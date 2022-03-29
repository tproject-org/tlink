from rest_framework import routers
from django.urls import path, include
from .views import URLViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'url', URLViewSet)

from . import views

urlpatterns = [
    path('api/', include(router.urls)),
    path("u/<str:slugs>", views.url_redirect, name="redirect"),
    path("", views.register_url, name="register_url")
]