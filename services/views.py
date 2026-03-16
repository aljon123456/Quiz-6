from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from services.models import Service
from services.serializers import ServiceSerializer


class ServiceListView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


class ServiceDetailView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


class MechanicServiceManageView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ServiceSerializer
    
    def get_queryset(self):
        return Service.objects.filter(mechanic=self.request.user)
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


class MechanicServiceDetailView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, pk):
        try:
            service = Service.objects.get(pk=pk, mechanic=request.user)
            serializer = ServiceSerializer(service, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Service.DoesNotExist:
            return Response(
                {'error': 'Service not found or not owned by you'},
                status=status.HTTP_404_NOT_FOUND
            )
    
    def post(self, request):
        # Create new service
        data = request.data.copy()
        data['mechanic'] = request.user.id
        
        serializer = ServiceSerializer(data=data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        try:
            service = Service.objects.get(pk=pk, mechanic=request.user)
            
            # Don't allow changing mechanic
            data = request.data.copy()
            if 'mechanic' in data:
                del data['mechanic']
            
            serializer = ServiceSerializer(service, data=data, partial=True, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Service.DoesNotExist:
            return Response(
                {'error': 'Service not found or not owned by you'},
                status=status.HTTP_404_NOT_FOUND
            )
    
    def delete(self, request, pk):
        try:
            service = Service.objects.get(pk=pk, mechanic=request.user)
            service.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Service.DoesNotExist:
            return Response(
                {'error': 'Service not found or not owned by you'},
                status=status.HTTP_404_NOT_FOUND
            )
