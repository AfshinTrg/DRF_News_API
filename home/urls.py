from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeNews.as_view()),
]