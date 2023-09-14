from django.urls import path
from .views import RegisterAPIView, ActivationAPIView, ChangePasswordAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('activate/<uuid:activation_code>/', ActivationAPIView.as_view()),
    path('refresh/', ChangePasswordAPIView.as_view())

]
