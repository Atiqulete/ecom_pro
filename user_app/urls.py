from django.urls import path
from user_app.views import register

urlpatterns = [
    path('register/',register,name='register'),
]
