# urls.py
from django.urls import path, include
from rest_framework import routers
from .views import MyModelViewSet  # Ensure correct import

router = routers.DefaultRouter()
router.register('call', MyModelViewSet)  # Register the viewset with the router

urlpatterns = [
    path('', include(router.urls)),
]