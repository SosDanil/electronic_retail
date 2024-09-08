from rest_framework import serializers

from companies.models import Company, Product
from companies.validators import DontUpdateDebtValidator


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = '__all__'


class CompanyUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'
        validators = [
            DontUpdateDebtValidator(field='debt'),
        ]


