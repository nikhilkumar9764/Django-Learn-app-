from django.http import JsonResponse
from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404


from django.http import HttpResponse
@api_view(['GET'])
def get_employee_list(request):

    if request.method == 'GET':
        employee_list = Employee.objects.all()
        la = EmployeeSerializer(employee_list, many=True).data
        return Response(la,status=status.HTTP_200_OK)

@api_view(['POST'])
def create(request):
    if request.method == 'POST':
        emp_serializer = EmployeeSerializer(data=request.data)
        if emp_serializer.is_valid():
            emp_serializer.save()
            print(emp_serializer.data)
            return Response(emp_serializer.data, status=status.HTTP_200_OK)

        return Response(emp_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def student_detail(request,id):
    emp = get_object_or_404(Employee, pk=id)

    if request.method == 'GET':
        emp_serializer = EmployeeSerializer(emp)
        return Response(emp_serializer.data)

    elif request.method == 'PUT':
        emp_serializer = EmployeeSerializer(emp,data=request.data)
        if emp_serializer.is_valid():
            emp_serializer.save()
            return Response(emp_serializer.data,status=status.HTTP_200_OK)

        return Response(emp_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        emp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)