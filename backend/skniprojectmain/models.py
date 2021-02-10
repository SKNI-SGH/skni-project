from django.db import models


class Company(models.Model):
    id = models.IntegerField(primary_key=True)
    company_name = models.CharField(max_length=999)
    full_name = models.CharField(max_length=999)
    industry = models.CharField(max_length=999)

    def __str__(self):
       return self.company_name



class Measure(models.Model):
    id = models.IntegerField(primary_key=True)
    value_name = models.CharField(max_length=999)

    def __str__(self):
       return self.value_name


class CompanyMeasure(models.Model):
    id_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    id_measure = models.ForeignKey(Measure, on_delete=models.CASCADE)

    end_date = models.DateTimeField()
    value = models.FloatField()

    def __str__(self):
        return self.value


class FinancialIndicator(models.Model):
    id = models.IntegerField(primary_key=True)
    indicator_name = models.CharField(max_length=999)
    indicator_type = models.CharField(max_length=999)

    def __str__(self):
        return self.indicator_name


class FinancialIndicatorMeasure(models.Model):
    id = models.IntegerField(primary_key=True)
    id_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    indicator_value = models.IntegerField()
    date = models.DateTimeField()
    id_indicators = models.ForeignKey(FinancialIndicator, on_delete=models.CASCADE)

    def __str__(self):
        return self.id

