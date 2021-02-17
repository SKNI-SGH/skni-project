from django.http import HttpResponse
from django.template import loader
from .models import CompanyMeasure
from django.shortcuts import render




def company_measures(request):
    company_measure_list = CompanyMeasure.objects.order_by('id_company')
    template = loader.get_template('skniprojectmain/measures.html') # tu trzeba bedzie wpisac sciezke do szablonu
    context = {
        'company_measure_list': company_measure_list,
    }
    #return render(request, 'measures.html',context)
    return HttpResponse(template.render(context, request))
    #output = ', '.join([str(q.value) for q in company_measure_list])
    #return HttpResponse(output)

