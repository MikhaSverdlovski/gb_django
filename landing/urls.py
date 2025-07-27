from django.contrib import admin
from django.urls import path, include
from .views import HomePageView, InfoPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', InfoPageView.as_view(), name='about'),
]