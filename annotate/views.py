from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from .models import Company, CompanySynonym, News, Patent, Tech, TechSynonym, Finance, KeywordsCompany, KeywordsTech
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.db.models.functions import Lower
import json
# Create your views here.

# ----------------------------- view for vue ajax request ----------------
# def home(request):
#     return render(request, "annotate/home.html")


def company_list_ajax(request):
    data = json.loads(request.body.decode('utf-8'))
    is_all = True if data["is_all"] == "2" else False
    print("is_all:", is_all)
    d = []
    data = {}
    if is_all:
        keywords = KeywordsCompany.objects.order_by(
            "is_labeled", Lower("name"))
    else:
        keywords = KeywordsCompany.objects.filter(is_labeled=False)

    for k in keywords:
        d.append(dict(id=k.pk, name=k.name, news_nums=k.news.count()))
    data["companys"] = d
    print(data)
    return JsonResponse(data)


def tech_list_ajax(request):
    data = json.loads(request.body.decode('utf-8'))
    is_all = True if data["is_all"] == "2" else False
    d = []
    data = {}
    if is_all:
        keywords = KeywordsTech.objects.order_by("is_labeled", Lower("name"))
    else:
        keywords = KeywordsTech.objects.filter(is_labeled=False)
    print("keywords-tech\n", keywords)
    for k in keywords:
        d.append(dict(id=k.pk, name=k.name, news_nums=k.news.count(),
                      patent_nums=k.patent.count()))
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


def news_company_list_ajax(request, kw):
    d = []
    data = {}
    news = KeywordsCompany.objects.get(name=kw).news.all()
    for n in news:
        d.append(dict(id=n.id, title=n.title, link=n.link, source=n.source))

    data["news"] = d
    print(data)
    return JsonResponse(data)


def news_tech_list_ajax(request, kw):
    d = []
    data = {}
    news = KeywordsTech.objects.get(name=kw).news.all()
    for n in news:
        d.append(dict(id=n.id, title=n.title, link=n.link, source=n.source))
    data["news"] = d
    print(data)
    return JsonResponse(data)


def patent_list_ajax(request, kw):
    d = []
    data = {}
    patents = KeywordsTech.objects.get(name=kw).patent.all()
    for p in patents:
        d.append(dict(id=p.id, name=p.name, author=p.author, status=p.status))
    data["patents"] = d
    print(data)
    return JsonResponse(data)


def keywords_company_delete_ajax(request, kw):
    print("kw is:", kw)
    data = {}
    data["state"] = "error"
    kw = get_object_or_404(KeywordsCompany, name=kw)
    try:
        kw.delete()
    except Exception as e:
        print(e)
    else:
        data["state"] = "success"
    finally:
        return JsonResponse(data)


def keywords_tech_delete_ajax(request, kw):
    print("kw is:", kw)
    data = {}
    data["state"] = "error"
    kw = get_object_or_404(KeywordsTech, name=kw)
    try:
        kw.delete()
    except Exception as e:
        print(e)
    else:
        data["state"] = "success"
    finally:
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
    try:
        company = Company.objects.get(name=company)
    except Exception as e:
        print(e)
    # if use 404 not reach here
    else:
        print("company", company)
        company_synonym = company.companysynonym_set.all()
        for c in company_synonym:
            d.append(dict(name=c.name))
    finally:
        data["company_synonym"] = d
        print(data)
        return JsonResponse(data)


def tech_synonym_list_ajax(request, tech):
    d = []
    data = {}
    try:
        tech = Tech.objects.get(name=tech)
    except Exception as e:
        print(e)
    else:
        tech_synonym = tech.techsynonym_set.all()
        for t in tech_synonym:
            d.append(dict(name=t.name))
    finally:
        data["tech_synonym"] = d
        print(data)
        return JsonResponse(data)


# @csrf_exempt
def company_add_ajax(request, company):
    data = json.loads(request.body.decode('utf-8'))
    print("company", company)
    print("data:", data)
    kw = KeywordsCompany.objects.get(name=data["kw"])
    company_syn = data["company_syn"]
    # 去除空值
    # company_syn = (cs for cs in company_syn if cs)
    print("company_syn:", company_syn)
    print("type:", type(company_syn))
    try:
        c = Company.objects.get(name=company)
    except Exception as e0:
        c = Company.objects.create(name=company)
    finally:
        print("kw:", kw)
        kw.is_labeled = True
        kw.save()
        try:
            for cs in company_syn:  # 去除空值
                if cs:
                    try:
                        CompanySynonym.objects.get(name=cs, company=c)
                    except Exception as e1:
                        CompanySynonym.objects.create(name=cs, company=c)
            return JsonResponse({"state": "success"})
        except Exception as e2:
            print(e2)
            return JsonResponse({"state": "error"})


# @csrf_exempt
def tech_add_ajax(request, tech):
    data = json.loads(request.body.decode('utf-8'))
    print("data:", data)
    kw = KeywordsTech.objects.get(name=data["kw"])
    tech_syn = data["tech_syn"]
    # 去除空值
    # company_syn = (cs for cs in company_syn if cs)
    try:
        t = Tech.objects.get(name=tech)
    except Exception as e0:
        t = Tech.objects.create(name=tech)
    finally:
        print("kw:", kw)
        kw.is_labeled = True
        kw.save()
        try:
            for ts in tech_syn:  # 去除空值
                if ts:
                    try:
                        TechSynonym.objects.get(name=ts, tech=t)
                    except Exception as e1:
                        TechSynonym.objects.create(name=ts, tech=t)
            return JsonResponse({"state": "success"})
        except Exception as e2:
            print(e2)
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
