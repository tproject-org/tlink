from rest_framework import routers, serializers, viewsets

from .models import URL

# Serializers define the API representation.
class UrlSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = URL
        fields = ('url', 'short_url', 'owner')

