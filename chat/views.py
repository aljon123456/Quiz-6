from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.conf import settings
from .serializers import ChatMessageSerializer

class AIChatbotView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        serializer = ChatMessageSerializer(data=request.data)
        if serializer.is_valid():
            user_message = serializer.validated_data['message']
            
            try:
                # Check if API key is configured
                api_key = settings.OPENAI_API_KEY
                
                if not api_key or api_key == '':
                    # Demo response when API key is not configured
                    demo_responses = {
                        'booking': 'You can book any of our services by selecting a mechanic and choosing your preferred time. We accept PayPal payments for your convenience.',
                        'price': 'Our prices vary by service. Oil changes start at $50, tire service at $80, and brake service at $120. Contact a mechanic for exact pricing.',
                        'mechanic': 'We have qualified mechanics available 24/7. All our mechanics are verified and have excellent ratings.',
                        'service': 'We offer mobile service including oil changes, tire replacement, brake service, battery replacement, and air filter replacement.',
                        'payment': 'We accept PayPal payments. You can securely pay through our payment integration.',
                        'default': 'I\'m a mobile mechanic support assistant. I can help you with booking services, pricing, mechanic qualifications, payments, and service information. What can I help you with?'
                    }
                    
                    # Simple keyword matching for demo
                    user_msg_lower = user_message.lower()
                    bot_response = demo_responses['default']
                    
                    if any(word in user_msg_lower for word in ['book', 'schedule', 'appointment']):
                        bot_response = demo_responses['booking']
                    elif any(word in user_msg_lower for word in ['price', 'cost', 'how much']):
                        bot_response = demo_responses['price']
                    elif any(word in user_msg_lower for word in ['mechanic', 'technician']):
                        bot_response = demo_responses['mechanic']
                    elif any(word in user_msg_lower for word in ['service', 'offer']):
                        bot_response = demo_responses['service']
                    elif any(word in user_msg_lower for word in ['payment', 'pay', 'paypal']):
                        bot_response = demo_responses['payment']
                    
                    return Response({
                        'message': user_message,
                        'response': bot_response
                    }, status=status.HTTP_200_OK)
                
                # Use OpenAI API if key is available
                try:
                    from openai import OpenAI
                    
                    client = OpenAI(api_key=api_key)
                    response = client.chat.completions.create(
                        model="gpt-4o-mini",
                        messages=[
                            {
                                "role": "system",
                                "content": """You are a helpful customer support chatbot for a Mobile Mechanic Service Marketplace. 
You help users with questions about:
- Booking services from mechanics
- Service pricing and availability
- Mechanic qualifications
- Vehicle service types (oil changes, tire replacement, brake service, etc.)
- Account and order management
- PayPal payments

Keep responses concise and friendly. If a user asks something unrelated to mobile mechanic services, politely redirect them to relevant topics."""
                            },
                            {
                                "role": "user",
                                "content": user_message
                            }
                        ],
                        max_tokens=500,
                        temperature=0.7,
                    )
                    
                    bot_response = response.choices[0].message.content
                    return Response({
                        'message': user_message,
                        'response': bot_response
                    }, status=status.HTTP_200_OK)
                
                except ImportError:
                    # Fallback if openai library not installed
                    return Response({
                        'message': user_message,
                        'response': 'Chat service temporarily unavailable. Please try again later.'
                    }, status=status.HTTP_200_OK)
                    
            except Exception as e:
                return Response({
                    'error': f'Chatbot service error: {str(e)}',
                    'message': 'Our support team is unavailable. Please contact us directly.'
                }, status=status.HTTP_200_OK)  # Return 200 with friendly message instead of 500
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
