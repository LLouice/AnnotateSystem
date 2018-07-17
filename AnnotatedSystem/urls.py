"""AnnotatedSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from annotate import views

# xadmin.autodiscover()

# version模块自动注册需要版本控制的 Model
# from xadmin.plugins import xversion
# xversion.register_models()

urlpatterns = [
    # path(r'', views.index, name="home"),
    path(r'', TemplateView.as_view(
        template_name="annotate/home.html"), name="home"),
    path(r'company_list_ajax', views.company_list_ajax, name="company_list_ajax"),
    path(r'tech_list_ajax', views.tech_list_ajax, name="tech_list_ajax"),
    path(r'finance_list_ajax', views.finance_list_ajax, name="finance_list_ajax"),
    path(r'news_list_ajax', views.news_list_ajax, name="news_list_ajax"),
    path(r'company/delete/<company>',
         views.company_delete_ajax, name="company_delete_ajax"),
    path(r'company_synonym_list/<company>',
         views.company_synonym_list_ajax, name="company_synonym_list_ajax"),
    path(r'tech_synonym_list/<tech>',
         views.tech_synonym_list_ajax, name="tech_synonym_list_ajax"),
    path(r'company/add/<company>',
         views.company_add_ajax, name="company_add_ajax"),


    # ------------------------------------------------
    path(r'index', views.index, name="index"),
    path(r'company_add/<company>',
         views.CompanyUpdateView.as_view(), name="company_add"),
    path(r'company/<pk>/delete',
         views.CompanyDeleteView.as_view(), name="company_delete"),
    path(r'company_synonym/<company>',
         views.CompanySynonymListView.as_view(), name="company_synonym"),
    # path(r'index', views.index, name="company_delete")
    path(r'news_detail/<company>',
         views.news_detail, name="news_detail"),
    path(r'news_list/<company>',
         views.NewsListView.as_view(), name="news_list"),
    path(r'news/<int:pk>', views.NewsDetailView.as_view(), name="news"),
    path(r'ajax/news/<company>', views.news_ajax, name="news_ajax"),
    path('admin/', admin.site.urls),
]
