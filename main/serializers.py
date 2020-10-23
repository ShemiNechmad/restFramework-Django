from rest_framework import serializers
from main.models import AppUsers


class AppUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUsers
        fields = ('firstName', 'lastName', 'age', 'married',)