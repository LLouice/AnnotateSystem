from django.contrib import admin
from .models import Company, CompanySynonym, News, Patent, Tech, TechSynonym, Finance, KeywordsCompany, KeywordsTech

# Register your models here.


class KeywordsCompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "is_labeled")
    list_filter = ["is_labeled"]


class KeywordsTechAdmin(admin.ModelAdmin):
    list_display = ("name", "is_labeled")
    list_filter = ["is_labeled"]

admin.site.register(KeywordsCompany, KeywordsCompanyAdmin)
admin.site.register(KeywordsTech, KeywordsTechAdmin)
admin.site.register((Company, CompanySynonym, News,
                     Patent, Tech, TechSynonym, Finance))
