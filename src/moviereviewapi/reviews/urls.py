########################

# this file is created by user

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, MovieViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'movies', MovieViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
