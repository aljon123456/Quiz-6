from rest_framework import serializers
from services.models import Service


class ServiceSerializer(serializers.ModelSerializer):
    mechanic_name = serializers.SerializerMethodField()
    mechanic_id = serializers.CharField(source='mechanic.id', read_only=True)
    sample_image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Service
        fields = [
            'id', 'mechanic', 'mechanic_id', 'mechanic_name', 'service_name', 
            'description', 'price', 'duration_of_service', 'sample_image',
            'sample_image_url', 'rating', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def get_mechanic_name(self, obj):
        return f"{obj.mechanic.first_name} {obj.mechanic.last_name}".strip() or obj.mechanic.username
    
    def get_sample_image_url(self, obj):
        request = self.context.get('request')
        if obj.sample_image:
            image_url = obj.sample_image.url
            if request:
                return request.build_absolute_uri(image_url)
            return image_url
        return None
