from django.urls import include, path
from employees import views

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('add/', views.employee_create, name='employee_add'),
    path('edit/<int:pk>/', views.employee_update, name='employee_edit'),
    path('delete/<int:pk>/', views.employee_delete, name='employee_delete'),
]
