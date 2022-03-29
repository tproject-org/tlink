from django.shortcuts import render

from rest_framework import viewsets

# Create your views here.

from .models import URL
from .serializers import URLSerializer

# ViewSets define the view behavior.
class URLViewSet(viewsets.ModelViewSet):
    queryset = URL.objects.all()
    serializer_class = URLSerializer

