from django.contrib import admin
from .models import ServiceOrder, ServiceCategory, Services


@admin.register(ServiceOrder)
class ServiceOrderAdmin(admin.ModelAdmin):
    model = ServiceOrder
    fields = [
        'client_name', 'client_cellphone', 'car_model',
        'car_plate', 'service_price', 'service', 'paid', 'created_at',
        'observation', 'cpf'
    ]

    search_fields = ['client_name', 'car_plate']
    readonly_fields = []
    ordering = ['client_name']


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    model = ServiceCategory
    fields = [
        'category_name'
    ]


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    model = Services
    fields = [
        'service', 'service_category'
    ]
    list_filter = ('service_category',)
