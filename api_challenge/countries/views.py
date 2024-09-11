from rest_framework import generics, status, pagination
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from .models import Country
from .serializers import CountrySerializer, CountryCreateSerializer


# Defines paginated response
class CustomPagination(pagination.LimitOffsetPagination):
    limit_query_param = 'limit'
    offset_query_param = 'offset'

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link(),
            },
            'pagination': {
                'count': self.count,
                'offset': self.offset,
                'limit': self.limit,
            },
            'results': data
        })


# Retrieve or update a specific country by ID
class CountryDetailView(generics.RetrieveUpdateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    def get_object(self):
        try:
            return Country.objects.get(id=self.kwargs['pk'])
        except Country.DoesNotExist:
            raise NotFound(detail="Country not found", code=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        country = self.get_object()
        serializer = CountrySerializer(country, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


# List all countries or create a new one
class CountryListView(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    pagination_class = CustomPagination

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CountryCreateSerializer
        return CountrySerializer

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset().order_by('id')

        # query param
        country_code = request.query_params.get('country-code')
        if country_code:
            queryset = queryset.filter(countryCode=country_code)

        # using pagination
        page = self.paginate_queryset(queryset)
        if page:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
