from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import ArticleSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from django.core.paginator import Paginator
from rest_framework import generics, mixins, filters
from articles.permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User

from .models import Article
from django.db.models import Q


class ArticleView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'body']
    ordering = ['-created_at']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SingleArticleView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    authentication_classes = [JWTAuthentication]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer  


class UserArticleView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

        # Get single
    def get(self, request, username):
        user = User.objects.filter(username=username)
        articles = []

        if user.exists():
            articles = Article.objects.filter(user=user[0].id).order_by('-created_at')
        
        serializer = ArticleSerializer(articles, many=True)

        return Response({
            'data': serializer.data
        }, status = status.HTTP_200_OK)
