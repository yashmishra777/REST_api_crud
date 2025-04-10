from .views import AuthorViewSet,BookViewSet,CategoryViewSet
from rest_framework.routers import SimpleRouter
from django.urls import path, include
router = SimpleRouter()
# router.register(r’your_route_name’, YourViewSet)
router.register('author', AuthorViewSet)
router.register('book', BookViewSet)
router.register('category', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]