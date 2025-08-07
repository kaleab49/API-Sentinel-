from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ScanRequestSerializer
from .scanners.sql_injection import scan_sql_injection
from .scanners.auth import scan_broken_auth
from .scanners.rate_limit import scan_rate_limiting
from .scanners.data_exposure import scan_data_exposure
from .scanners.misconfig import scan_misconfig

# Create your views here.

class ScanAPIView(APIView):
    def post(self, request):
        serializer = ScanRequestSerializer(data=request.data)
        if serializer.is_valid():
            url = serializer.validated_data['url']
            headers = serializer.validated_data.get('headers', {})
            results = [
                scan_sql_injection(url, headers),
                scan_broken_auth(url, headers),
                scan_rate_limiting(url, headers),
                scan_data_exposure(url, headers),
                scan_misconfig(url, headers),
            ]
            return Response({"results": results})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
