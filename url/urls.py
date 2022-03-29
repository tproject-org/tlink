from rest_framework import routers
from django.urls import path, include
from .views import URLViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'url', URLViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]