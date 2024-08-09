# views.py
from rest_framework import viewsets
from .models import MyModel
from .seralizers import MyModelSerializer  # Ensure correct import

class MyModelViewSet(viewsets.ModelViewSet):  # Use a capitalized class name
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer