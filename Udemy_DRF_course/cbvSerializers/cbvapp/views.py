from django.shortcuts import render
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Employee
from .serializer import EmployeeSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework import mixins,generics


class EmployeeList(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


'''
class EmployeeList(mixins.ListModelMixin , mixins.CreateModelMixin , generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self,request):
        return self.list(request)

    def post(self,request):
        return self.create(request)

class EmployeeDetail(mixins.RetrieveModelMixin , mixins.UpdateModelMixin , mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)
'''


'''
class EmployeeListView(APIView):
    def get(self,request):
        employee_list = Employee.objects.all()
        la = EmployeeSerializer(employee_list, many=True).data
        return Response(la, status=status.HTTP_200_OK)

    def post(self,request):
        emp_serializer = EmployeeSerializer(data=request.data)
        if emp_serializer.is_valid():
            emp_serializer.save()
            print(emp_serializer.data)
            return Response(emp_serializer.data, status=status.HTTP_200_OK)

        return Response(emp_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeDetailView(APIView):
    def get(self,request,id):
        emp = get_object_or_404(Employee, pk=id)
        emp_serializer = EmployeeSerializer(emp)
        return Response(emp_serializer.data)

    def put(self,request,id):
        emp = get_object_or_404(Employee, pk=id)
        emp_serializer = EmployeeSerializer(emp, data=request.data)
        if emp_serializer.is_valid():
            emp_serializer.save()
            return Response(emp_serializer.data, status=status.HTTP_200_OK)

        return Response(emp_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        emp = get_object_or_404(Employee, pk=id)
        emp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
'''