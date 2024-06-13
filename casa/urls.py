
from django.urls import path
from casa import views

urlpatterns = [
    path('', views.home),
]