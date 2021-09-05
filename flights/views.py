from rest_framework import viewsets, status, generics, mixins
from rest_framework.response import Response
from .models import Flight
from .serializers import FlightSerializer


class FlightsViewSet(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

    def get(self, request):
        return self.list(request)


