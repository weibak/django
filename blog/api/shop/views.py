from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from api.shop.serializers import PurchaseModelSerializer, PurchaseCreateSerializer
from shop.models import Purchase, Product


class UserPurchaseViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    """
    API endpoint that allows get purchases.
    """

    queryset = Purchase.objects.all()
    serializer_class = PurchaseModelSerializer
    permission_classes = []


class PurchaseCreateView(CreateAPIView):
    """
    API endpoint that allows to create users.
    """

    serializer_class = PurchaseCreateSerializer
    permission_classes = []

    def perform_create(self, serializer):
        user = User(
            username=serializer.validated_data["email"],
            email=serializer.validated_data["email"],
        )
        product = Product(
            id=serializer.validated_data["product"]
        )
        count = serializer.validated_data["count"]
        Purchase.objects.create(user=user, product=product, count=count)
