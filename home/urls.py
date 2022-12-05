from django.urls import path
from . import views

urlpatterns = [
    path('', views.AddNewsView.as_view()),
    path('panel/', views.PanelView.as_view()),
]
