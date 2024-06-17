
from django.urls import path
from casa.views import views

urlpatterns = [
    path('', views.login_view),
    path('home/', views.home, name='home'),
    path('upload_foto/', views.upload_foto, name='upload_foto'),
    path('mostrar_foto/', views.mostrar_foto, name='mostrar_foto'),
    path('some_view/', views.some_view, name='some_view'),
]