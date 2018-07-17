from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from .models import Company, CompanySynonym, News, Patent, Tech, TechSynonym, Finance
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse, HttpResponse
from django.core import serializers
import json
# Create your views here.

# ----------------------------- view for vue ajax request ----------------
# def home(request):
#     return render(request, "annotate/home.html")


def company_list_ajax(request):
    d = []
    data = {}
    companys = Company.objects.all()
    for c in companys:
        d.append(dict(id=c.pk, name=c.name, news_nums=c.news_set.count()))
    data["companys"] = d
    print(data)
    return JsonResponse(data)


def tech_list_ajax(request):
    d = []
    data = {}
    techs = Tech.objects.all()
    print("techs\n", techs)
    for t in techs:
        d.append(dict(id=t.pk, name=t.name, news_nums=t.news_set.count(),
                      patent_nums=t.patent_set.count()))
    data["techs"] = d
    print(data)
    return JsonResponse(data)


def finance_list_ajax(request):
    '''
        新闻标题
        来源
        投资方
        关系
        融资方
    '''
    d = []
    data = {}
    finance = Finance.objects.all()
    for f in finance:
        news = f.news_set.all()
        news_count = news.count()
        news = news.first()
        d.append(dict(id=f.pk, invest=f.company_from.name, invested=f.company_to_id, level=f.level,
                      news_id=news.id, news_title=news.title, news_link=news.link, news_nums=news_count))
    data["finance"] = d
    print(data)
    return JsonResponse(data)


def news_list_ajax(request):
    company_name = request.POST.get("company")
    company = get_object_or_404(Company, name=company)
    news = company.news_set.all()
    data = {}
    data["news"] = news
    return JsonResponse(data)


def company_delete_ajax(request, company):
    data = {}
    company = get_object_or_404(Company, name=company)
    try:
        company.delete()
    except Exception as e:
        data["state"] = "error"
    else:
        data["state"] = "success"
    finally:
        return JsonResponse(data)


def company_synonym_list_ajax(request, company):
    d = []
    data = {}
    company = get_object_or_404(Company, name=company)
    company_synonym = company.companysynonym_set.all()
    for c in company_synonym:
        d.append(dict(name=c.name))
    data["company_synonym"] = d
    print(data)
    return JsonResponse(data)


def tech_synonym_list_ajax(request, tech):
    d = []
    data = {}
    tech = get_object_or_404(Tech, name=tech)
    tech_synonym = tech.techsynonym_set.all()
    for t in tech_synonym:
        d.append(dict(name=t.name))
    data["tech_synonym"] = d
    print(data)
    return JsonResponse(data)


@csrf_exempt
def company_add_ajax(request, company):
    data = json.loads(request.body.decode('utf-8'))
    print("company", company)
    print("data:", data)
    company_syn = data["company_syn"]
    print("company_syn:", company_syn)
    print("type:", type(company_syn))
    try:
        c = Company.objects.get(name=company)
    except Exception as e0:
        c = Company.objects.create(name=company)
    finally:
        try:
            for cs in company_syn:
                try:
                    CompanySynonym.objects.get(name=cs, company=c)
                except Exception as e1:
                    CompanySynonym.objects.create(name=cs, company=c)
            return JsonResponse({"state": "success"})
        except Exception as e2:
            print(e1)
            return JsonResponse({"state": "error"})


# -------------------------------- view for django template --------------


def index(request):
    # 企业实体表格
    company = Company.objects.all()
    # global news_src
    # for c in company:
    #     new_src = c.news_set.all()
    #     patent_src = c.patent_set.all()
    #     synonym = c.companysynonym_set.all()
    #     new_src_count = len(new_src)
    #     patent_src_count = len(patent_src)

    return render(request, "annotate/index.html", {"company": company})


def news_detail(request, company):
    company = get_object_or_404(Company, name=company)

    # print("news", news)
    news = company.news_set.all()
    return render(request, "annotate/news_detail.html", {"news": news})


def company_delete(request, company):
    company = get_object_or_404(Company, name=company)
    company.delete()
    return redirect("index")


def company_synonym_add(request, company):
    company = get_object_or_404(Company, name=company)
    return redirect("index")


class CompanySynonymListView(ListView):
    model = CompanySynonym
    template_name = "annotate/company_synonym.html"
    context_object_name = "company_synonym"

    def get_queryset(self):
        queryset = super(CompanySynonymListView, self).get_queryset()
        queryset = queryset.filter(company=self.kwargs["company"])

        return queryset


class CompanyUpdateView(UpdateView):
    model = Company

    def post(self, request, *args, **kwargs):
        pass


@method_decorator(csrf_exempt, name='dispatch')
class CompanyDeleteView(DeleteView):
    model = Company
    success_url = reverse_lazy('index')

    def get_queryset(self):
        print("调用get_queryset")
        # queryset = super(CompanyDeleteView, self).get_queryset()
        queryset = Company.objects.all()  # TODO
        return queryset

    def post(self, request, *args, **kwargs):
        print("调用post")
        reponse = super().post(self, request, *args, **kwargs)
        return JsonResponse({'state': 'success'})

    def form_invalid(self, form):
        print("调用form_invalid")
        response = super().form_invalid(form)
        if self.request.is_ajax():
            data = {
                'state': 'error'
            }
            return JsonResponse(data, status=400)
        else:
            return response

    def form_valid(self, form):
        print("调用form_valid")
        response = super().form_valid(form)
        if self.request.is_ajax():
            data = {
                'state': 'success'
            }
            return JsonResponse(data)
        else:
            return response


def news_ajax(request, company):
    company = get_object_or_404(Company, name=company)
    # # print("news", news)
    news = company.news_set.all()
    # news = company.news_set.values()
    # news = simplejson.dumps(news)
    # news = {"A": "alijid", "B": "bupt"}

    # news = serializers.serialize("json", news)
    # 要显示的新闻字段 id title link
    news = news.values("id", "title", "link")

    # return HttpResponse(news)
    return JsonResponse({"data": list(news)})


class NewsListView(ListView):
    model = News
    context_object_name = "news_list"
    template_name = "annotate/news_list.html"

    def get_queryset(self):
        # queryset = super(NewsListView, self).get_queryset()
        company = get_object_or_404(Company, name=self.kwargs["company"])
        queryset = company.news_set.all()
        print("正在调用get_queryset")
        return queryset


class NewsDetailView(DetailView):
    model = News
    template_name = "annotate/news.html"
    context_object_name = "news"
