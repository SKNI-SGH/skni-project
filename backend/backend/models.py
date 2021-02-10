from django.db import models


class Company(models.Model):
    id = models.IntegerField(primary_key=True)
    company_name = models.CharField()
    full_name = models.CharField()
    industry = models.CharField()


class Measure(models.Model):
    id = models.IntegerField(primary_key=True)
    value_name = models.CharField()


class CompanyMeasure(models.Model):
    id_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    id_measure = models.ForeignKey(Measure, on_delete=models.CASCADE)

    end_date = models.TimeField()
    value = models.FloatField()


class FinancialIndicator(models.Model):
    id = models.IntegerField(primary_key=True)
    indicator_name = models.CharField()
    indicator_type = models.CharField()


class FinancialIndicatorMeasure(models.Model):
    id = models.IntegerField(primary_key=True)
    id_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    indicator_value = models.IntegerField()
    date = models.DateTimeField()
    id_indicators = models.ForeignKey(FinancialIndicator, on_delete=models.CASCADE)

