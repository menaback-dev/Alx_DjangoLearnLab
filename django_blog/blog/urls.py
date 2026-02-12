from django.urls import path, include
from . import views
from .views import (
    home,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)


urlpatterns = [
    path('', home, name='home'),
    path('login/',views.login, name='login'),
    path("post/", PostListView.as_view(), name="post-list"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('accounts/', include('django.contrib.auth.urls')),
]
