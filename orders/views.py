from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from orders.models import Order
from orders.serializers import OrderSerializer


class CreateOrderView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        customer = request.user
        service_id = request.data.get('service')
        paypal_transaction_id = request.data.get('paypal_transaction_id')
        total_cost = request.data.get('total_cost')
        scheduled_date = request.data.get('scheduled_date')
        location = request.data.get('location')
        
        # Validate required fields
        if not all([service_id, paypal_transaction_id, total_cost]):
            return Response(
                {'error': 'Missing required fields: service, paypal_transaction_id, total_cost'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Check for duplicate transaction ID
        if Order.objects.filter(paypal_transaction_id=paypal_transaction_id).exists():
            return Response(
                {'error': 'Order with this transaction ID already exists'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            order = Order.objects.create(
                customer=customer,
                service_id=service_id,
                paypal_transaction_id=paypal_transaction_id,
                total_cost=total_cost,
                scheduled_date=scheduled_date,
                location=location,
            )
            serializer = OrderSerializer(order)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )


class UserOrderHistoryView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer
    
    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user).order_by('-date_purchased')
