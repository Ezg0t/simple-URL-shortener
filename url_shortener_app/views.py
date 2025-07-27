from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import URL
from .serializers import URLSerializer
from rest_framework.response import Response

class ShortenURLView(generics.CreateAPIView):
    queryset = URL.objects.all()
    serializer_class = URLSerializer

class ExpandURLView(APIView):
    def get(self, request, short_code: str) -> Response:
        try:
            short_url = URL.objects.get(short_code=short_code)
            return Response({"url": short_url.url})
        except URL.DoesNotExist:
            return Response({"error": "URL not found"}, status=status.HTTP_404_NOT_FOUND)