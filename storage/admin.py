from django.contrib import admin
from .models import CategoryStorage, Storage


@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'category')
    search_fields = ['name']
    readonly_fields = ('id',)
    ordering = ('name',)
    list_filter = ('category', 'quantity')
