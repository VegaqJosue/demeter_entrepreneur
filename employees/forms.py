from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'employee_code',
            'first_name',
            'second_name',
            'third_name',
            'first_surname',
            'second_surname',
            'document_name',
            'document_id',
            'photo',
            'credit_limit',
        ]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for name, field in self.fields.items():
            if self.errors.get(name):
                field.widget.attrs.update({'class': 'form-control is-invalid'})
            else:
                field.widget.attrs.update({'class': 'form-control'})