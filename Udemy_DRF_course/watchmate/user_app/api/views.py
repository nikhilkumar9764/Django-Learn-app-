from rest_framework.views import *
from rest_framework.decorators import api_view

from .serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token


@api_view(['POST', ])
def registration_view(request):
    if request.method == 'POST':
       serializer = RegistrationSerializer(data=request.data)
       data = {}

       if serializer.is_valid():
           account = serializer.save()
           data['response'] = 'Registration successful'
           data['email'] = account.email
           data['username'] = account.username
       else:
           data['errors'] = serializer.errors

       return Response(data, status=status.HTTP_201_CREATED)
