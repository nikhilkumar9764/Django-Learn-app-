from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.ListEmployees.as_view(), name = 'getall_employees'),
    path('employees/<int:pk>', views.EmployeeDetail.as_view(), name='employee_detail'),
    path('books/', views.ListBooks.as_view(), name='getall_books'),
    path('books/<int:pk>', views.BookDetail.as_view(), name='book_detail'),
]