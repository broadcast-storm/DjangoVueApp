from rest_framework import serializers
from .models import Article, JobPosition, UserType, Division


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ["id", "title", "content", "picture", "created_at", "updated_at"]


class JobPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosition
        fields = ["id", "title", "description"]


class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserType
        fields = ["id", "title", "description"]


class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Division
        fields = ["id", "title", "description"]
