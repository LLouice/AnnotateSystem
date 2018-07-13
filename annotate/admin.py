from django.contrib import admin
from .models import Company, CompanySynonym, News, Patent, Tech, TechSynonym, Finance

# Register your models here.
admin.site.register((Company, CompanySynonym, News,
                     Patent, Tech, TechSynonym, Finance))
