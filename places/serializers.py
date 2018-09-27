from rest_framework import serializers


class PlaceSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128)
    address = serializers.CharField(max_length=254)
    website = serializers.CharField(max_length=128)
    contact_number = serializers.CharField(max_length=15)
