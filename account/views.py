from django.shortcuts import render
from .serializers import RegisterSerializer
from django.contrib.auth.models import User
from rest_framework import mixins, generics


class RegisterView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
