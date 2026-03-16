from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from uuid import uuid4
from applications.models import MechanicApplication
from applications.serializers import MechanicApplicationSerializer
from users.models import CustomUser


class SubmitApplicationView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        user = request.user
        
        # Check if user already has an application
        if MechanicApplication.objects.filter(user=user).exists():
            return Response(
                {'error': 'You have already submitted an application'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        application = MechanicApplication.objects.create(user=user)
        serializer = MechanicApplicationSerializer(application)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ListApplicationView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MechanicApplicationSerializer
    queryset = MechanicApplication.objects.all()
    
    def get_queryset(self):
        if self.request.user.role != 'admin':
            return MechanicApplication.objects.none()
        return MechanicApplication.objects.all()


class ApproveApplicationView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, pk):
        if request.user.role != 'admin':
            return Response(
                {'error': 'Only admins can approve applications'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        try:
            application = MechanicApplication.objects.get(pk=pk)
            user = application.user
            
            # Update user role to mechanic
            user.role = 'mechanic'
            
            # Generate merchant_id if not already set
            if not user.merchant_id:
                user.merchant_id = uuid4().hex[:12].upper()
            
            user.save()
            
            # Update application status
            application.status = 'approved'
            application.save()
            
            serializer = MechanicApplicationSerializer(application)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except MechanicApplication.DoesNotExist:
            return Response(
                {'error': 'Application not found'},
                status=status.HTTP_404_NOT_FOUND
            )


class DeclineApplicationView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, pk):
        if request.user.role != 'admin':
            return Response(
                {'error': 'Only admins can decline applications'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        try:
            application = MechanicApplication.objects.get(pk=pk)
            reason = request.data.get('decline_reason', '')
            
            application.status = 'declined'
            application.decline_reason = reason
            application.save()
            
            serializer = MechanicApplicationSerializer(application)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except MechanicApplication.DoesNotExist:
            return Response(
                {'error': 'Application not found'},
                status=status.HTTP_404_NOT_FOUND
            )
