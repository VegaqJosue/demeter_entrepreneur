from django import forms
from .models import Tenant

class Tenantform(forms.ModelForm):

    class Meta:
        model = Tenant
        fields = [
            "legal_name",
            "comercial_name",
            "logo_url",
            "default_currency",
            "timezone",
            "active"
        ]