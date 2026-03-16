from rest_framework import serializers
from applications.models import MechanicApplication
from users.models import CustomUser


class MechanicApplicationSerializer(serializers.ModelSerializer):
    user_email = serializers.CharField(source='user.email', read_only=True)
    user_name = serializers.SerializerMethodField()
    
    class Meta:
        model = MechanicApplication
        fields = ['id', 'user', 'user_email', 'user_name', 'status', 'decline_reason', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def get_user_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}".strip()
