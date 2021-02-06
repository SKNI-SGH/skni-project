from django.http import HttpResponse
from django.template import loader

import backend.backend.models as m


def index(request):
    company_measure_list = m.CompanyMeasure.objects.order_by('id_company')
    template = loader.get_template('templatePath') # tu trzeba bedzie wpisac sciezke do szablonu
    context = {
        'CompanyMeasureList': company_measure_list,
    }
    return HttpResponse(template.render(context, request))



