from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('tamrin/', views.tamrin, name='tamrin'),
    path('costumer/', views.comtumer),
    path('tamrin/<int:tamrin_id>/', views.detailTamrin, name='detail'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
]