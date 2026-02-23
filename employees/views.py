from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Employee
from .forms import EmployeeForm


@login_required
def employee_list(request):
    qs = Employee.objects.filter(active=True).order_by("employee_code")
    return render(request, "employees/list.html", {"employees": qs})


@login_required
def employee_form(request, pk=None):
    instance = get_object_or_404(Employee, pk=pk) if pk else None

    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect("employee_list")
    else:
        form = EmployeeForm(instance=instance)

    return render(request, "employees/form.html", {"form": form})


@login_required
def employee_delete(request, pk):
    emp = get_object_or_404(Employee, pk=pk)
    emp.active = False
    emp.save()
    return redirect("employee_list")
