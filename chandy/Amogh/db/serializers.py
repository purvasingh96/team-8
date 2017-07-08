from rest_framework import serializers
from models import CreateUser, Points


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Points
        fields = ('')

