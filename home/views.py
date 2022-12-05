from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import NewsSerializer
import requests
from rest_framework import status


class AddNewsView(APIView):

    def get(self, request):
        resp = requests.get('https://feeds.npr.org/1004/feed.json')
        items = resp.json()['items'][0:5]
        for item in items:
            item['author'] = item['author']['name'] if 'author' in item else None
            item['tags'] = '-'.join(item['tags']) if 'tags' in item else None
            item['attachments'] = str(item['attachments']) if 'attachments' in item else None
        srz_data = NewsSerializer(data=items, many=True, partial=True)
        if srz_data.is_valid():
            srz_data.create(srz_data.validated_data)
            return Response('items added', status=status.HTTP_201_CREATED)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)
