from django.shortcuts import render
from .serializers import RegisterSerializer
from django.contrib.auth.models import User
from rest_framework import mixins, generics
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class RegisterView(mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = RegisterSerializer
    
    def get(self, request):
        users = User.objects.filter(username=request.user)
        serializer = RegisterSerializer(users[0])

        return Response(serializer.data, status = status.HTTP_200_OK)
    
class PublicUserDetailsView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)