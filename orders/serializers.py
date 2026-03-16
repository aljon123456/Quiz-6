from rest_framework import serializers
from orders.models import Order
from services.serializers import ServiceSerializer


class OrderSerializer(serializers.ModelSerializer):
    service_detail = ServiceSerializer(source='service', read_only=True)
    mechanic_name = serializers.CharField(source='service.mechanic_name', read_only=True)
    service_name = serializers.CharField(source='service.service_name', read_only=True)
    
    class Meta:
        model = Order
        fields = [
            'id', 'customer', 'service', 'service_detail', 'service_name',
            'mechanic_name', 'paypal_transaction_id', 'total_cost',
            'scheduled_date', 'location', 'status', 'date_purchased'
        ]
        read_only_fields = ['id', 'customer', 'date_purchased']
