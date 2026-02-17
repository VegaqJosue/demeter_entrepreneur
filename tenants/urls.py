from django.urls import path
from . import views

urlpatterns = [
    path("", views.tenant_list, name="tenant_list"),
    path("create/", views.tenant_create, name="tenant_create"),
    path("update/<uuid:pk>/", views.tenant_update, name="tenant_update"),
    path("delete/<uuid:pk>/", views.tenant_delete, name="tenant_delete"),
]