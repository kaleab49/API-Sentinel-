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
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework import serializers

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

class RegisterAPIView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            if User.objects.filter(username=username).exists():
                return Response({'error': 'Username already exists.'}, status=400)
            user = User.objects.create_user(username=username, password=password)
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response(serializer.errors, status=400)

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
