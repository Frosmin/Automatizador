
from django.urls import path
from casa.views import views
from .views.viewsPDF import some_view



urlpatterns = [
    path('', views.login_view),
    path('home/', views.home, name='home'),
    path('upload_foto/', views.upload_foto, name='upload_foto'),
    path('mostrar_foto/', views.mostrar_foto, name='mostrar_foto'),
    path('some_view/', some_view, name='some_view'),

    path('subir_cemento', views.subir_cemento, name='subir_cemento'),
    path('seleccionar_casa/', views.seleccionar_casa, name='seleccionar_casa'),
]