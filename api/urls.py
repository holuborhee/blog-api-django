from django.urls import path
from account.views import RegisterView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from articles.views import ArticleView, SingleArticleView, UserArticleView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('users/<str:username>/articles/', UserArticleView.as_view()),
    path('articles/', ArticleView.as_view()),
    path('articles/<pk>/', SingleArticleView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]