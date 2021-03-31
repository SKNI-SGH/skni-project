from django.db import models


class Company(models.Model):
    id = models.IntegerField(primary_key=True)
    company_name = models.CharField(max_length=999)
    full_name = models.CharField(max_length=999)
    industry = models.CharField(max_length=999)





class Measure(models.Model):
    id = models.IntegerField(primary_key=True)
    value_name = models.CharField(max_length=999)



#id_companymeasure=models.IntegerField(primary_key=True)
class CompanyMeasure(models.Model):

    id_company = models.ForeignKey(Company,related_name='id_companymeasure', on_delete=models.CASCADE)
    id_measure = models.ForeignKey(Measure, on_delete=models.CASCADE)

    end_date = models.DateTimeField()
    value = models.FloatField()

  #  class Meta:
  #      unique_together = ['id_company', 'id_measure']
  #      ordering = ['id_measure']

  #  def __str__(self):
  #      return '%d: %s' % (self.end_date, self.value)




class FinancialIndicator(models.Model):
    id = models.IntegerField(primary_key=True)
    indicator_name = models.CharField(max_length=999)
    indicator_type = models.CharField(max_length=999)




class FinancialIndicatorMeasure(models.Model):
    id = models.IntegerField(primary_key=True)
    id_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    indicator_value = models.IntegerField()
    date = models.DateTimeField()
    id_indicators = models.ForeignKey(FinancialIndicator, on_delete=models.CASCADE)



