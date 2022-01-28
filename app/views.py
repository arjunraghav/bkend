from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle
from rest_framework.exceptions import Throttled
from django.contrib.auth.views import LoginView

from .serializers import FileSerializer
from .models import UserFile


class Login(LoginView):
    template_name = 'login.html'


class FileUploadViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    throttle_class = [UserRateThrottle]
    model = UserFile
    serializer_class = FileSerializer
    queryset = UserFile.objects.all()

    def create(self, request, *args, **kwargs):
        context = {}
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        qs = UserFile.objects.filter(id=serializer.data['id'])
        context["message"] = "file uploaded"
        for i in qs:
            context["upload_id"] = str(i)
        return Response(context, status=status.HTTP_201_CREATED, headers=headers)

    def throttled(self, request, wait):
        raise Throttled(detail={
            "message": "“Too many attempts",
        })
