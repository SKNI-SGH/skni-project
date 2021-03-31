from rest_framework import serializers


from .models import Company

class MeasureSerializer(serializers.ModelSerializer):
    id_companymeasure = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Company
        fields = ('id', 'company_name', 'full_name', 'industry', 'id_companymeasure')