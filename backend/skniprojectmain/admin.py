from django.contrib import admin

from .models import Company, Measure, CompanyMeasure, FinancialIndicator, FinancialIndicatorMeasure

admin.site.register(Company)
admin.site.register(Measure)
admin.site.register(CompanyMeasure)
admin.site.register(FinancialIndicator)
admin.site.register(FinancialIndicatorMeasure)



# Register your models here.
