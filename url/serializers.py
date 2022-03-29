from rest_framework import routers, serializers, viewsets

from .models import URL

# Serializers define the API representation.
class URLSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = URL
        fields = '__all__'

