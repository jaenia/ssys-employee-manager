# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('employee_edit', kwargs={'pk': self.pk})