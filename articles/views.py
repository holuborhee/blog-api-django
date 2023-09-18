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
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'body']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # def post(self, request):
        

    #     data = request.data
    #     data['user'] = request.user.id
    #     serializer = ArticleSerializer(data=data)

    #     if not serializer.is_valid():
    #         return Response({
    #             'data': serializer.errors,
    #             'message': 'Something went wrong'
    #         }, status = status.HTTP_400_BAD_REQUEST)
        
    #     serializer.save()

    #     return Response({
    #         'data': serializer.data,
    #         'message': 'Blog successfully created'
    #     }, status = status.HTTP_201_CREATED)
    
    # def get(self, request):
    #     articles = Article.objects.all()
    #     user = request.GET.get('user')
    #     search_term = request.GET.get('q')
    #     if user:
    #         articles = articles.filter(user=user)
        
    #     if search_term:
    #         articles = articles.filter(Q(title__icontains = search_term) | Q(body__icontains = search_term))

    #     serializer = ArticleSerializer(articles, many = True)

    #     return Response(serializer.data)
    # def get(self, request, *args, **kwargs):
    #     queryset = Article.objects.all()

    #     user = self.request.query_params.get('user')
    #     search_term = self.request.query_params.get('q')

    #     if user:
    #         queryset = queryset.filter(user=user)
        
    #     if search_term:
    #         queryset = queryset.filter(Q(title__icontains = search_term) | Q(body__icontains = search_term))
        
    #     return queryset

        

        

        # page = request.GET.get('page', 1)
        # paginator = Paginator(articles, 2)

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
            articles = Article.objects.filter(user=user[0].id)
        
        serializer = ArticleSerializer(articles, many=True)

        return Response({
            'data': serializer.data
        }, status = status.HTTP_200_OK)
    
# class SingleArticleView(APIView):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     authentication_classes = [JWTAuthentication]

    # fix password issue

    # Get single
    # def get(self, request, id):
    #     article = Article.objects.filter(id=id)
    #     if not article.exists():
    #         return Response({
    #             'data': {},
    #             'message': 'This article does not exist'
    #         }, status = status.HTTP_404_NOT_FOUND)
        
    #     serializer = ArticleSerializer(
    #         article[0]
    #     )

    #     return Response({
    #         'data': serializer.data
    #     }, status = status.HTTP_200_OK)

    # # update
    # def patch(self, request, id):
    #     article = Article.objects.filter(id=id)
    #     if not article.exists():
    #         return Response({
    #             'data': {},
    #             'message': 'This article does not exist'
    #         }, status = status.HTTP_404_NOT_FOUND)


    #     serializer = ArticleSerializer(
    #         article[0],
    #         data = request.data,
    #         partial = True
    #     )

    #     if not serializer.is_valid():
    #         return Response({
    #             'data': serializer.errors,
    #             'message': 'Something went wrong'
    #         }, status = status.HTTP_400_BAD_REQUEST)
        
    #     serializer.save()

    #     return Response({
    #         'data': serializer.data,
    #         'message': 'Article successfully updated'
    #     }, status = status.HTTP_200_OK)
    # # Delete
    # def delete(self, request, id):
    #     article = Article.objects.filter(id=id)
    #     if not article.exists():
    #         return Response({
    #             'data': {},
    #             'message': 'This article does not exist'
    #         }, status = status.HTTP_404_NOT_FOUND)
    #     article[0].delete()

    #     return Response({
    #         'data': {},
    #         'message': 'Article successfully deleted'
    #     }, status = status.HTTP_200_OK)