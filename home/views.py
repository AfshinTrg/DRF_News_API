from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import NewsSerializer
import requests
from rest_framework import status
from django.views import View
from .forms import PanelForm
from django.shortcuts import render
from .models import News


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


class PanelView(View):
    form_class = PanelForm
    template_name = 'home/login.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            news = News.objects.all()
            return render(request, 'home/news_list.html', {'news': news})
        return render(request, self.template_name, {'form': form})
