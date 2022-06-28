from rest_framework import serializers
from .models import User, Profession

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'mobile')

class ProfessionSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Profession
        fields = ('id', 'user', 'work', 'salary')        