from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),

    path('', views.index, name='index'),
    path('event/<str:pk>/', views.viewEvent, name='event'),
    path('add/', views.addEvent, name='add'),
]

    

