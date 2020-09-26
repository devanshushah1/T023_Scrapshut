from rest_framework import serializers
from login.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = '__all__'


class NgoSerializer(serializers.ModelSerializer):
    username = UserSerializer(read_only=True, many=True)

    class Meta():
        model = Ngo
        fields = '__all__'


class DonorSerializer(serializers.ModelSerializer):
    class Meta():
        model = Donor
        fields = '__all__'
