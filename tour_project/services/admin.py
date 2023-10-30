from django.contrib import admin
from .models import Country, Service, ServiceImage


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    list_editable = ['is_active']
    search_fields = ['name']


@admin.register(ServiceImage)
class ServiceImageAdmin(admin.ModelAdmin):
    list_display = ['service', 'id']
    list_filter = ['service']
    search_fields = ['service__name']

class ServiceImageInline(admin.TabularInline):
    model = ServiceImage
    extra = 1

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'price', 'duration_days']
    list_filter = ['country']
    search_fields = ['name', 'country__name']
    inlines = [ServiceImageInline]
