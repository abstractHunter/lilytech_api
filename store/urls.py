from django.urls import path, include
from rest_framework import routers
from .views import CategoryViewSet, ProductViewSet, api_root

router = routers.SimpleRouter()
router.register('category', CategoryViewSet, basename='category')
router.register('product', ProductViewSet, basename='product')


urlpatterns = [
    path('', api_root),
    path('', include(router.urls)),
]
