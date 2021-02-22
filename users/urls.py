from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('products/', views.products),
    path('costumer/', views.comtumer),
    path('login/', views.loginPage),
    path('register/', views.registerPage),
]