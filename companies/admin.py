from django.contrib import admin
from companies.models import Company, Product
from django_admin_relation_links import AdminChangeLinksMixin


@admin.register(Company)
class CompanyAdmin(AdminChangeLinksMixin, admin.ModelAdmin):
    list_display = ('name', 'email', 'country', 'city', 'street', 'house_number', 'type', 'level', 'supplier_link',
                    'debt')
    list_filter = ('type', 'level', 'city')
    search_fields = ('name', 'country')
    change_links = ('supplier',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'company', 'release_date')
    list_filter = ('company',)
    search_fields = ('name',)

