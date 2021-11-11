from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.Login,name='login'),
    path('register',views.register,name='register'),
    path('logout',views.Logout,name='logout'),
    path('post/<str:pk>',views.Post,name='post'),
]