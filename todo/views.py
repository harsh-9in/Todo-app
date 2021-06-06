from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .serializers import TaskSerializer
from .models import Task
from rest_framework_simplejwt.authentication import JWTAuthentication


class FeedViewset(viewsets.ModelViewSet):
    authentication_classes = (JWTAuthentication,)
    serializer_class = TaskSerializer
    def get_queryset(self):
        return Task.objects.filter(user_profile=self.request.user)
    permission_classes = [IsAuthenticated,]

    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user)


