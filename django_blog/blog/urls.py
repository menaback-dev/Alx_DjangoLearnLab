from django.urls import path, include
from . import views
from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('posts/', views.posts, name='posts'),
    path('register/', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
]
