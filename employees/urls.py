from django.urls import path
from . import views

urlpatterns = [
    path("", views.employee_list, name="employee_list"),
    path("form/", views.employee_form, name="employee_create"),
    path("form/<uuid:pk>/", views.employee_form, name="employee_update"),
    path("delete/<uuid:pk>/", views.employee_delete, name="employee_delete"),
]
