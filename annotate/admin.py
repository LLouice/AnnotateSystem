from django.contrib import admin
from .models import Company, CompanySynonym, News, Patent, Tech, TechSynonym, Finance, KeywordsCompany, KeywordsTech

# Register your models here.
admin.site.register((Company, CompanySynonym, News,
                     Patent, Tech, TechSynonym, Finance, KeywordsCompany, KeywordsTech))
