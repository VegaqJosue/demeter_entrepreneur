from django.contrib import admin
from .models import Tenant

@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ("comercial_name", "default_currency", "timezone", "active")
    search_fields = ("commercial_name", "legal_name")
    list_filter = ("active", "default_currency")