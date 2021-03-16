from django.urls import path
from . import views

urlpatterns = [

    # This if for GET & POS request for insertion of data.
    path('', views.employee_form, name = 'employee_insert'), 
    # GET request show the list of employees.
    path('list/', views.employee_list, name = 'employee_list'),
    # his if for GET & POS request Update the employee.
    path('<int:id>/', views.employee_form, name = 'employee_update'),
    path('delete/<int:id>/', views.employee_delete, name = 'employee_delete'),
    
]