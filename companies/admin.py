from django.contrib import admin

from companies.models import Company, Product


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'country', 'city', 'street', 'house_number', 'type', 'level', 'supplier', 'debt')
    ordering = ('name', 'country')
    list_filter = ('type', 'level')
    search_fields = ('name', 'country')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'company', 'release_date')
    ordering = ('name',)
    list_filter = ('company',)
    search_fields = ('name',)
