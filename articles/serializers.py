from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at', 'user']
        user = serializers.ReadOnlyField(source='user.username')
