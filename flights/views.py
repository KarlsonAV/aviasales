from rest_framework import viewsets, status, generics, mixins
from rest_framework.response import Response
from .models import Flight
from .serializers import FlightSerializer


class FlightsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
