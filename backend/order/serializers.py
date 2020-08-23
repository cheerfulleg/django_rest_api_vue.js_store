from rest_framework import serializers

from backend.items.serializers import ItemSerializer
from .models import OrderItem, Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'name', 'email',
                  'address', 'zip', 'city', 'paid',
                  'created']


class OrderItemSerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    products = ItemSerializer(many=True)

    class Meta:
        model = OrderItem
        fields = '__all__'
