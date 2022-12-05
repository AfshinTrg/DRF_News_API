from django.urls import path
from . import views

app_name = 'home'


urlpatterns = [
    path('', views.AddNewsView.as_view()),
    path('panel/', views.PanelView.as_view(), name='panel'),
]
