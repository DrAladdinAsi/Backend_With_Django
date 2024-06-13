from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,

)
from . import views
from .tokenSerializer import *


urlpatterns = [
    
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('profile/', views.getUserProfile, name='getUserProfile'),
    path('', views.getUsersProfile, name='getUsersProfile'),
    path('register/',views.registerUser , name='registerUser') ,
]
