from django.urls import path, include 
from .views import UserViewSet, ProfileViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("all", UserViewSet)
router.register("profiles", ProfileViewSet)
urlpatterns = router.urls
