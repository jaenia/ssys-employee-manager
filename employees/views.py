# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from employees.models import Employee
from employees.forms import EmployeeForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

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

# @csrf_exempt
# @api_view(["POST"])
# @permission_classes((AllowAny,))
# def login(request):
#     username = request.data.get("username")
#     password = request.data.get("password")
#     if username is None or password is None:
#         return Response(
#             {'error': 'Please provide both username and password'},
#             status=HTTP_400_BAD_REQUEST
#         )
#     user = authenticate(username=username, password=password)
#     if not user:
#         return Response(
#             {'error': 'Invalid Credentials'},
#             status=HTTP_404_NOT_FOUND
#         )
#     token = Token.objects.get_or_create(user=user)
#     return Response(
#         {'token': token.key},
#         status=HTTP_200_OK
#     )
