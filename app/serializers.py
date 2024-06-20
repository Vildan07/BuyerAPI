from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Buyer


class BuyerSerializer(serializers.ModelSerializer):
    """
    This Serializer serializes the Buyer model
    """
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Buyer
        fields = '__all__'
        read_only_fields = ('user',)
