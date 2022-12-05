from rest_framework import serializers
from .models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

    def create(self, validated_data):
        return News.objects.create(**validated_data)

