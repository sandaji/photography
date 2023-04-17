from django.urls import path
from photography.views import register_user
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import LoginView

urlpatterns = [
    path('api/users/', register_user, name='register_user'),
    # app/urls.py
    path('login/', LoginView.as_view(), name='login'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


]
