# users/urls.py
from django.urls import path
from .views import register, MyTokenObtainPairView, MyTokenRefreshView, logout

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', MyTokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', MyTokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', logout, name='logout'),
]
