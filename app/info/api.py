from .models import UserProfile
from rest_framework import viewsets, permissions
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer
