from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import Flight, Airport


class AirportSerializer(ModelSerializer):
    class Meta:
        model = Airport
        fields = [
            'code',
            'city',
        ]


class FlightSerializer(ModelSerializer):
    origin = AirportSerializer()
    destination = AirportSerializer()

    class Meta:
        model = Flight
        fields = [
            'origin',
            'destination',
            'duration',
            'ticket_price',
            'amount_of_passengers',
        ]