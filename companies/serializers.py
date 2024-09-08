from rest_framework import serializers

from companies.models import Company, Product


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'


class CompanyUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        exclude = ['debt',]


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
