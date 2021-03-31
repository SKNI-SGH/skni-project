#from django.http import HttpResponse
#from django.template import loader
from .models import CompanyMeasure
#from django.shortcuts import render
from django.http import JsonResponse
#import json

from rest_framework import viewsets


from .serializers import MeasureSerializer
from .models import Company

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all().order_by('id')
    serializer_class = MeasureSerializer





