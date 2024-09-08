from django.urls import path

from companies.apps import CompaniesConfig
from companies.views import CompanyCreateAPIView, CompanyListAPIView, CompanyRetrieveAPIView, CompanyUpdateAPIView, \
    CompanyDestroyAPIView

app_name = CompaniesConfig.name

urlpatterns = [
    path('create/', CompanyCreateAPIView.as_view(), name='create_company'),
    path('', CompanyListAPIView.as_view(), name='list_company'),
    path('retrieve/<int:pk>/', CompanyRetrieveAPIView.as_view(), name='retrieve_company'),
    path('update/<int:pk>/', CompanyUpdateAPIView.as_view(), name='update_company'),
    path('delete/<int:pk>/', CompanyDestroyAPIView.as_view(), name='delete_company'),
]
