from django.urls import include, path
from rest_framework import routers
from employees import views
from employees.api import viewsets
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'employees', viewsets.EmployeeViewSet)

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('employees/', include('employees.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]