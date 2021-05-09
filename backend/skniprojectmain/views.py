#from django.http import HttpResponse
#from django.template import loader
from .models import CompanyMeasure
#from django.shortcuts import render
from django.http import JsonResponse
#import json
from rest_framework import viewsets

from .serializers import MeasureSerializer, CompanyMeasureSerializer, CompanySerializer
from .models import Company, Measure

#class CompanyViewSet(viewsets.ModelViewSet):
#    queryset = Company.objects.all().order_by('id')
 #   serializer_class = MeasureSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    # queryset = Measure.objects.all().order_by('id')
    # serializer_class = MeasureSerializer
     queryset = Company.objects.all().order_by('id')
     serializer_class = CompanySerializer








#def company_measures(request):
 #   company_measure_list = CompanyMeasure.objects.order_by('id_company')
    #template = loader.get_template('skniprojectmain/measures.html') # tu trzeba bedzie wpisac sciezke do szablonu

 #   context = [{ 'value_name': str(cm.id_measure.value_name), 'company_name': str(cm.id_company.company_name),
  #               'value_date': [{'data': cm.end_date, 'value': cm.value}, {'data': cm.end_date, 'value': cm.value}, {'data': cm.end_date, 'value': cm.value}] }
  #                 for cm in company_measure_list]
        #'company_measure_list': company_measure_list
#'value_date' : {'value': str(cm.value), 'end_date': str(cm.end_date),'value1': str(cm.value), 'end_date1': str(cm.end_date), 'value2': str(cm.value), 'end_date2': str(cm.end_date)  } }



    #return render(request, 'measures.html',context)
   # return JsonResponse(context, safe=False)
    #output = ', '.join([str(q.value) for q in company_measure_list])
    #return HttpResponse(output)

