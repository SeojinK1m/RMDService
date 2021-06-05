from API.models import School, Eatery, Review
from API.serializers import SchoolSerializer, EaterySerializer, ReviewSerializer
from rest_framework import viewsets, filters

# Create your views here.
class EateryViewset(viewsets.ModelViewSet):
    queryset = Eatery.objects.all()
    serializer_class = EaterySerializer
    lookup_field = 'url'
    search_fields = ['school__id']
    filter_backends = (filters.SearchFilter,)

class SchoolsViewset(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    lookup_field = 'url'
    search_fields = ['name', 'url']
    filter_backends = (filters.SearchFilter,)


class ReviewViewset(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    search_fields = ['eatery__id']
    filter_backends = (filters.SearchFilter,)