from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Buyer
from .serializers import BuyerSerializer
from .filters import BuyerFilter
from .permissions import AuthorOrReadOnly
from .paginations import BuyerPagination


# Create your views here.


class BuyerViewSet(ModelViewSet):
    """
    ViewSet for Buyer Model
    """
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = BuyerFilter
    search_fields = ['title', 'description']
    ordering_fields = ['date', 'user']
    permission_classes = [AuthorOrReadOnly]
    pagination_class = BuyerPagination

