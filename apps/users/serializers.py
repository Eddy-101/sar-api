from rest_framework import serializers

from .models import (User, UserCondition)

class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCondition
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    condition = ConditionSerializer(many=True)

    class Meta:
        model = User
        fields = (
            'id',
            'name',
            'surname',
            'objective_weight',
            'state',
            'condition',
        )

