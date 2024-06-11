from rest_framework import serializers
from news.models import Category, News, User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["password"]


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"