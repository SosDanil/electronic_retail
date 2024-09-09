from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from companies.models import Company, Product
from companies.serializers import CompanySerializer, CompanyUpdateSerializer, ProductSerializer, CompanyCreateSerializer


class CompanyCreateAPIView(CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyCreateSerializer


class CompanyListAPIView(ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [SearchFilter,]
    search_fields = ['country',]


class CompanyRetrieveAPIView(RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyUpdateAPIView(UpdateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyUpdateSerializer


class CompanyDestroyAPIView(DestroyAPIView):
    queryset = Company.objects.all()


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
