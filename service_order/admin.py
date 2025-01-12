from django.contrib import admin
from .models import ServiceOrder


@admin.register(ServiceOrder)
class ServiceOrderAdmin(admin.ModelAdmin):
    model = ServiceOrder
    fields = [
        'client_name', 'client_cellphone', 'car_model',
        'car_plate', 'service_price', 'service', 'service1', 'paid', 'created_at',
        'observation', 'cpf'
    ]

    search_fields = ['client_name', 'car_plate']
    readonly_fields = ['created_at']
    ordering = ['client_name']
