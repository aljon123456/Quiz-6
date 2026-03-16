from rest_framework import serializers
from .models import ServiceReview
from users.models import CustomUser

class ServiceReviewSerializer(serializers.ModelSerializer):
    reviewer_name = serializers.SerializerMethodField()
    
    class Meta:
        model = ServiceReview
        fields = ['id', 'service', 'reviewer', 'reviewer_name', 'rating', 'comment', 'created_at']
        read_only_fields = ['id', 'reviewer', 'created_at']
    
    def get_reviewer_name(self, obj):
        return obj.reviewer.username
