from rest_framework import serializers
from rest_framework.serializers import Serializer


class BasketItemSerializer(Serializer):
    product_id = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    qty = serializers.IntegerField()
    total_price = serializers.SerializerMethodField()

    @staticmethod
    def get_total_price(obj):
        return obj['price'] * obj['qty']


class BasketSerializer(Serializer):
    items = BasketItemSerializer(many=True)
    total_price = serializers.SerializerMethodField()
    total_qty = serializers.SerializerMethodField()

    @staticmethod
    def get_total_price(obj):
        return sum(item['total_price'] for item in obj['items'])

    @staticmethod
    def get_total_qty(obj):
        return sum(item['qty'] for item in obj['items'])
