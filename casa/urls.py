
from django.urls import path
from casa import views

urlpatterns = [
    path('', views.login_view),
    path('home/', views.home, name='home'),
    path('upload_foto/', views.upload_foto, name='upload_foto'),
]