from rest_framework import serializers
from orders.models import Orders, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['menu_item', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Orders
        fields = ['id', 'customer', 'restaurant', 'status', 'items', 'created_at']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Orders.objects.create(**validated_data)

        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)

        return order
