from django.urls import path, include

from rest_framework import routers

from .views import BuyerViewSet


router = routers.DefaultRouter()
router.register('buyer', BuyerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]