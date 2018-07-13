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
from annotate import views

# xadmin.autodiscover()

# version模块自动注册需要版本控制的 Model
# from xadmin.plugins import xversion
# xversion.register_models()

urlpatterns = [
    path(r'', views.index, name="home"),
    path(r'index', views.index, name="index"),
    path(r'company_add/<company>', views.CompanyUpdateView.as_view(), name="company_add"),
    path(r'company/<pk>/delete', views.CompanyDeleteView.as_view(), name="company_delete"),
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
