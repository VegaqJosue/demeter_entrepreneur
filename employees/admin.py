from django.contrib import admin
from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("employee_code", "first_name", "first_surname", "credit_limit", "active")
    search_fields = ("employee_code", "first_name", "first_surname", "document_id")
    list_filter = ("active",)