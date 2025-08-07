from django.urls import path
from .views import ScanAPIView, RegisterAPIView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('scan/', ScanAPIView.as_view(), name='scan'),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),
] 