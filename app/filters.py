from django_filters.rest_framework import FilterSet

from .models import Buyer


class BuyerFilter(FilterSet):
    class Meta:
        model = Buyer
        fields = ['date']