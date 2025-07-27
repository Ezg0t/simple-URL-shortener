from rest_framework import serializers
from .models import URL
from rest_framework.request import Request as DRFRequest
from typing import Optional

class URLSerializer(serializers.ModelSerializer):
    short_url = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = URL
        fields = ['url', 'short_url']
        extra_kwargs = {
        'url': {'write_only': True},
    }
        
    def create(self, validated_data):
        existing: Optional[URL] = URL.objects.filter(url=validated_data['url']).first()
        if existing:
            return existing
        return super().create(validated_data)
        
    def get_short_url(self, obj: URL) -> str:
        request: Optional[DRFRequest] = self.context.get('request')
        if request:
            return request.build_absolute_uri(f'/shrt/{obj.short_code}/')
        return f'/shrt/{obj.short_code}/'