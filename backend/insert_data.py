import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

import skniprojectmain.models as m
import datetime as dt
import random as rn
import string

sd = ((1, 'MSFT', 'Microsoft corp.', 'IT')
               , (1, 'P/E')
               , (dt.datetime.today(), 4.25)
               , (1, 'ROE', 'R')
               , (1, 1, 0.1, dt.datetime.today(), 1))


def fill_single_company(sample_data):

    company = m.Company.objects.create(id=sample_data[0][0], company_name=sample_data[0][1]
                                       , full_name=sample_data[0][2], industry=sample_data[0][3])

    company.save()


    measure = m.Measure.objects.create(id=sample_data[1][0], value_name=sample_data[1][1])

    measure.save()


    company_measure = m.CompanyMeasure.objects.create(id_company=company, id_measure=measure
                                                      , end_date=sample_data[2][0], value=sample_data[2][1])

    company_measure.save()


    fin_ind = m.FinancialIndicator.objects.create(id=sample_data[3][0], indicator_name=sample_data[3][1]
                                                  , indicator_type=sample_data[3][2])

    fin_ind.save()


    fin_ind_m = m.FinancialIndicatorMeasure.objects.create(id=sample_data[4][0], id_company=company
                                                           , indicator_value=sample_data[4][2], date=sample_data[4][3]
                                                           , id_indicators=fin_ind)





    fin_ind_m.save()


def create_sample_data(how_many):
    sample_data_list = []

    for e in range(how_many):
        name = ''.join(rn.sample(string.ascii_letters, 8))
        short_name = name[:3].upper()
        industry = rn.choice(['IT', 'EN', 'HC'])

        id_mea = e
        id_name = rn.choice(['P/E', 'P/BV'])

        fin_ind = rn.choice(['ROE', 'DPS', 'ROA'])

        new_company = ((e, short_name, name, industry)
                       , (id_mea, id_name)
                       , (dt.datetime.today(), rn.randint(3, 15))
                       , (e, fin_ind, 'R')
                       , (e, e, rn.randint(1, 10)/10, dt.datetime.today(), e))

        sample_data_list.append(new_company)

    return sample_data_list


for company in create_sample_data(100):
    fill_single_company(company)

