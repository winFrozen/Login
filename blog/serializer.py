import string
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import *

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = '__all__'
    def validate(self, data):
        password = data.get('password', None)
        if len(password) < 8:
            raise ValidationError(
                {
                    'status': False,
                    'message': "Parol juda qisqa"
                }
            )
        return data









