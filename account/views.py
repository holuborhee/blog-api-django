from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer


class RegisterView(APIView):

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({
                'data': serializer.errors,
                'message': 'Something went wrong'
            }, status = status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response({
            'data': {},
            'message': 'Your account is created'
        }, status = status.HTTP_201_CREATED)
