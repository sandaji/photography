from django.urls import path
from photography.views import register_user

urlpatterns = [
    path('api/users/', register_user, name='register_user'),
]
