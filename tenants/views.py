from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Tenant
from .forms import Tenantform

@login_required
#Get all tenants in the DB
def tenant_list(request):
    if request.user.user_scope == "TENANT":
        ls_tenants = Tenant.objects.filter(id=request.user.tenant_id, active=True)
    else:
        ls_tenants = Tenant.objects.all()
    
    return render(request, "tenants/list.html", {'tenants': ls_tenants})

@login_required
#Create a new tenant in the database
def tenant_create(request):
    if request.user.user_scope != "PLATFORM":
        return redirect("home")

    if request.method == "POST":
        form = Tenantform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("tenant_list")
    else:
        form = Tenantform()
    return render(request, "tenants/form.html", {"form": form})

@login_required
def tenant_update(request,pk):
    if request.user.user_scope != "PLATFORM":
        return redirect("home")
    
    tenant = get_object_or_404(Tenant, pk=pk)

    if request.method == "POST":
        form = Tenantform(request.POST, request.FILES, instance=tenant)
        if form.is_valid():
            form.save()
            return redirect("tenant_list")
    else:
        form = Tenantform(instance=tenant)

    return render(request, "tenants/form.html", {"form": form})

@login_required
def tenant_delete(request, pk):
    if request.user.user_scope != "PLATFORM":
        return redirect("home")
    
    tenant = get_object_or_404(Tenant, pk=pk)
    tenant.active = False
    tenant.save()
    return redirect("tenant_list")