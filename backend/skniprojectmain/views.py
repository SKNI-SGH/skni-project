from django.http import HttpResponse
from django.template import loader
from .models import CompanyMeasure



def index(request):
    company_measure_list = CompanyMeasure.objects.order_by('id_company')
    #template = loader.get_template('templatePath') # tu trzeba bedzie wpisac sciezke do szablonu
    context = {
        'CompanyMeasureList': company_measure_list,
    }
   # return HttpResponse(template.render(context, request))

    return HttpResponse('abc')

