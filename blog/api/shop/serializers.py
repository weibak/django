from rest_framework import serializers

from shop.models import Purchase


class PurchaseModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Purchase
        fields = (
            "id",
            "count",
            "product_id",
            "user_id",
            "created_at"
        )
        read_only_fields = ("id", "date_joined")


class PurchaseCreateSerializer(serializers.Serializer):
    email = serializers.EmailField()
    product = serializers.IntegerField()
    count = serializers.IntegerField()
