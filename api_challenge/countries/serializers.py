from rest_framework import serializers
from .models import Country


class CountryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['name', 'country_code']


class CountrySerializer(serializers.ModelSerializer):
    group_id = serializers.IntegerField(allow_null=True)
    created_at = serializers.DateTimeField()

    class Meta:
        model = Country
        fields = ['id', 'name', 'country_code', 'created_at', 'group_id']


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
