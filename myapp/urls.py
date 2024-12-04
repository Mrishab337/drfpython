from django.urls import path,include
from rest_framework.routers import  DefaultRouter
from .views import BusinessregisterViewSet
router = DefaultRouter()
router.register('api',BusinessregisterViewSet)

urlpatterns = [
    path('',include(router.urls))
]