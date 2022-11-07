from rest_framework import serializers

from rest_framework.validators import ValidationError
from .models import (User, Status)

from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=5, write_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'name',
            'surname',
            'age',
            'email',
            'password',
            'image',
            'description',
            'objective_weight',
            'state',
        )

    def validate(self, attrs):
        verify_email = User.objects.filter(email=attrs['email']).exists()

        if verify_email:
            return ValidationError("Email is al ready used")

        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop("password")

        user = super().create(validated_data)
        
        user.set_password(password)

        user.save()

        Token.objects.create(user=user)

        return user

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status 
        fields = (
            'id',
            'date', 
            'weight',
            'height',
            'hip',
            'waist',
            'minimum_pressure',
            'maximum_pressure',
            'imc',
            'user'
        )
