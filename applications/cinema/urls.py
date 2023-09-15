from django.urls import path, include
from applications.cinema.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('', PostAPIView)

urlpatterns = [

]

urlpatterns += router.urls