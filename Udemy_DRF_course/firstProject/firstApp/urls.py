from django.urls import path
from . import views

urlpatterns = [
    path('getall', views.get_employee_list, name = 'getall_employees'),
    path('create/', views.create , name= 'create_employee'),
    path('get_detail/<int:id>/', views.student_detail, name='get_employee_detail')
]