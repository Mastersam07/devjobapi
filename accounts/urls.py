from django.urls import path

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from .custom_claims import MyTokenObtainPairView
from .views import registration

urlpatterns = [
    path("register/", registration, name="register"),
    path('login/', MyTokenObtainPairView.as_view(), name="login"),
    path('token/refresh/', TokenRefreshView.as_view(), name="token"),
]