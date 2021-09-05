from django.db import models
from users.models import User


class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} - ({self.code})"


class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()
    ticket_price = models.IntegerField(default=20, blank=True)

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"

    @property
    def amount_of_passengers(self):
        return self.passengers.all().count()


class Passenger(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE, related_name='person')
    flights = models.ManyToManyField(Flight, blank=True, related_name='passengers')

    def __str__(self):
        return f"{self.person.first_name} {self.person.last_name}"