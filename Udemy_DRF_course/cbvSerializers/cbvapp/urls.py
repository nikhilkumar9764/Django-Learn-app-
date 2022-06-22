from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employees/' , views.EmployeeList.as_view()),
   path('employees/<int:pk>' , views.EmployeeDetail.as_view())
]