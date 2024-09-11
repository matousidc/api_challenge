from rest_framework import serializers
from .models import Country


class CountryCreateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True, max_length=255)
    countryCode = serializers.CharField(required=True, max_length=3)
    
    class Meta:
        model = Country
        fields = ['name', 'countryCode']


class CountrySerializer(serializers.ModelSerializer):
    groupId = serializers.IntegerField(allow_null=True)
    createdAt = serializers.DateTimeField()

    class Meta:
        model = Country
        fields = ['id', 'name', 'countryCode', 'createdAt', 'groupId']


class LinksSerializer(serializers.Serializer):
    next = serializers.URLField(allow_blank=True, required=False)
    previous = serializers.URLField(allow_blank=True, required=False)


class PaginationSerializer(serializers.Serializer):
    count = serializers.IntegerField(min_value=0)
    offset = serializers.IntegerField(min_value=0)
    limit = serializers.IntegerField(min_value=0)


class CollectionResultSerializer(serializers.Serializer):
    links = LinksSerializer()
    pagination = PaginationSerializer()


class CountriesSerializer(CollectionResultSerializer):
    results = CountrySerializer(many=True)

    class Meta:
        fields = ['links', 'pagination', 'results']
