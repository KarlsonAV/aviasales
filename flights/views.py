from rest_framework import viewsets, filters, generics
from rest_framework.response import Response
from .models import Flight
from .serializers import FlightSerializer


class FlightsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class FlightSearchView(generics.ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=origin__code', '=destination__code']
