from django.contrib import admin
from client.models import Client


@admin.register(Client)
class AdminClient(admin.ModelAdmin):
    model = Client

    list_display = [
        'client_name', 'cellphone', 'car_model', 'car_plate', 'created_at'
    ]
    readonly_fields = ['created_at']
    search_fields = ['client_name', 'cellphone']

    fieldsets = (
        ('Client Information', {
            'fields': ('client_name', 'cellphone')
        }),
        ('Car Information', {
            'fields': ('car_model', 'car_plate')
        }),
        ('Created_at', {
            'fields': ('created_at',)
        })
    )
