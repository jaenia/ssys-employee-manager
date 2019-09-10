# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from employees.models import Employee
from employees.forms import EmployeeForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

@login_required
def employee_list(request):
    employee = Employee.objects.all()
    data = {}
    data['object_list'] = employee
    return render(request, 'employee_list.html', data)
    
@login_required
def employee_create(request):
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('employee_list')
    return render(request, 'employee_form.html', {'form':form})

@login_required
def employee_update(request, pk):
    employee= get_object_or_404(Employee, pk=pk)
    form = EmployeeForm(request.POST or None, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('employee_list')
    return render(request, 'employee_form.html', {'form':form})

@login_required
def employee_delete(request, pk):
    employee= get_object_or_404(Employee, pk=pk)    
    if request.method=='POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employee_confirm_delete.html', {'object':employee})
