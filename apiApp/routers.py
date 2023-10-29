from rest_framework.routers import DefaultRouter
from .viewset import ProductViewset


router = DefaultRouter()
router.register('api-router', ProductViewset, basename='api-d')

urlpatterns= router.urls