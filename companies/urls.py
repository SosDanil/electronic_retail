from django.urls import path
from rest_framework import routers

from companies.apps import CompaniesConfig
from companies.views import CompanyCreateAPIView, CompanyListAPIView, CompanyRetrieveAPIView, CompanyUpdateAPIView, \
    CompanyDestroyAPIView, ProductViewSet

app_name = CompaniesConfig.name

router = routers.DefaultRouter()
router.register('products', ProductViewSet)

urlpatterns = [
    path('create/', CompanyCreateAPIView.as_view(), name='create_company'),
    path('', CompanyListAPIView.as_view(), name='list_company'),
    path('retrieve/<int:pk>/', CompanyRetrieveAPIView.as_view(), name='retrieve_company'),
    path('update/<int:pk>/', CompanyUpdateAPIView.as_view(), name='update_company'),
    path('delete/<int:pk>/', CompanyDestroyAPIView.as_view(), name='delete_company'),
] + router.urls
