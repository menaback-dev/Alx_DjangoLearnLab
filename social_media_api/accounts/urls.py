from django.urls import path
from .views import RegisterView, LoginView, ProfileView, follow_user, unfollow_user

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('profile/', ProfileView.as_view()),
    path('follow/<int:user_id>/', follow_user),
    path('unfollow/<int:user_id>/', unfollow_user),
]
