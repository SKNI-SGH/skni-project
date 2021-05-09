from rest_framework import serializers
import pickle

from .models import Company, CompanyMeasure, Measure


#class MeasureSerializer(serializers.ModelSerializer):
#    id_companymeasure = serializers.PrimaryKeyRelatedField(many=True, read_only=True) # serializer do wyświetlania wszystkich, related serializers
#    class Meta:
#        model = Company
#        fields = ('id', 'company_name', 'full_name', 'industry')




class CompanySerializer(serializers.ModelSerializer):
    measures = serializers.SerializerMethodField()

    def get_measures(self, company):


        measures ={}
        for cm in company.companymeasure_set.all():
            measures[cm.id_measure.value_name]=cm.value

        return measures

    class Meta:
        model = Company
        fields = ['company_name', 'full_name', 'industry', 'id', 'measures']

class MeasureSerializer(serializers.ModelSerializer):
    #companyMeasures = CompanyMeasureSerializer(many=False, read_only=True) #zmienić

    class Meta:
        model = Measure
        fields = ['value_name']

class CompanyMeasureSerializer(serializers.ModelSerializer):
    company = CompanySerializer(many=False, read_only=True, source='id_company')
    measure = MeasureSerializer(many=False, read_only=True, source='id_measure')
    measures = serializers.SerializerMethodField()
    dictionary = {Measure.value_name: CompanyMeasure.value}
    serial_dictionary=pickle.dumps(dictionary)
    # class CompanyMeasureListingField:
    #     def __init__(self, value):
    #         return '%d: %s' % (value.value_name, value.value)

    class Meta:
        model = CompanyMeasure
        # abc = model.value

        fields = ['end_date', 'value', 'company', 'id_measure', 'measure','measures' ]


