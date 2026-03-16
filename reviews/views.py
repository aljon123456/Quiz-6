from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from .models import ServiceReview
from .serializers import ServiceReviewSerializer
from services.models import Service

class CreateServiceReviewView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, service_id):
        try:
            service = Service.objects.get(id=service_id)
        except Service.DoesNotExist:
            return Response({'error': 'Service not found'}, status=status.HTTP_404_NOT_FOUND)
        
        # Check if review already exists
        existing_review = ServiceReview.objects.filter(
            service=service, reviewer=request.user
        ).first()
        
        if existing_review:
            return Response({
                'error': 'You have already reviewed this service'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = ServiceReviewSerializer(data={
            'service': service.id,
            'reviewer': request.user.id,
            'rating': request.data.get('rating'),
            'comment': request.data.get('comment', ''),
        })
        
        if serializer.is_valid():
            serializer.save(reviewer=request.user, service=service)
            # Update service rating
            reviews = Service.objects.filter(id=service_id).first().reviews.all()
            avg_rating = sum(r.rating for r in reviews) / len(reviews) if reviews else 0
            Service.objects.filter(id=service_id).update(rating=avg_rating)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetServiceReviewsView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request, service_id):
        try:
            service = Service.objects.get(id=service_id)
        except Service.DoesNotExist:
            return Response({'error': 'Service not found'}, status=status.HTTP_404_NOT_FOUND)
        
        reviews = ServiceReview.objects.filter(service=service).order_by('-created_at')
        serializer = ServiceReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
