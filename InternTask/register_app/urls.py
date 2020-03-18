from django.contrib import admin
from django.urls import path
from register_app import views

# TEMPLATE URLs
app_name = 'register_app'

# URL Patterns
urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('user_login', views.user_login, name='user_login'),
    path('user_logout', views.user_logout, name="user_logout"),
]
