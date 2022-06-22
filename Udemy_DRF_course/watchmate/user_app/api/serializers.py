from rest_framework import serializers
from django.contrib.auth.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        p1 = self.validated_data['password']
        p2 = self.validated_data['password2']

        if p1 != p2:
            raise serializers.ValidationError({'error' : 'password1 and password2 are not same'})

        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error': 'email already exists'})

        account = User(username=self.validated_data['username'], email=self.validated_data['email'])
        account.set_password(p1)
        account.save()

        return account
