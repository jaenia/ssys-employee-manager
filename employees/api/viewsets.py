# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from employees.models import Employee
from employees.api.serializers import EmployeeSerializer
from rest_framework import viewsets


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
