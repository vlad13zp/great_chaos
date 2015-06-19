from rest_framework import serializers

from mazypages.models import Route


class RouteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Route
        fields = ('start_route', 'end_route', )
