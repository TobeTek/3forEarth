from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model

from .serializers import SponsorSerializer, CompanySerializer

class CreateSponsorView(CreateAPIView):
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SponsorSerializer

class CreateCompanyView(CreateAPIView):
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CompanySerializer