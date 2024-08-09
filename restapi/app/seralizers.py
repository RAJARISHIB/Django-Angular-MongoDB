# serializers.py
from rest_framework import serializers
from .models import MyModel  # Ensure you import the correct model

class MyModelSerializer(serializers.ModelSerializer):  # Use a capitalized class name
    class Meta:
        model = MyModel
        fields = '__all__'