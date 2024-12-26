from django.db import models
from django.contrib.auth.models import User


class AstronomyShow(models.Model):
    title = models.CharField(max_length=63, blank=True)
    description = models.TextField(max_length=255)
    themes = models.ManyToManyField("ShowTheme", related_name="astronomy_shows")

    def __str__(self):
        return self.title


class ShowTheme(models.Model):
    name = models.CharField(max_length=63, blank=True)

    def __str__(self):
        return self.name


class PlanetariumDome(models.Model):
    name = models.CharField(max_length=63)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    def __str__(self):
        return self.name


class ShowSession(models.Model):
    astronomy_show = models.ForeignKey(AstronomyShow, on_delete=models.CASCADE, related_name="sessions")
    planetarium_dome = models.ForeignKey(PlanetariumDome, on_delete=models.CASCADE, related_name="sessions")
    show_time = models.DateTimeField()

    def __str__(self):
        return f"{self.astronomy_show} at {self.show_time}"


class Reservation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reservations")

    def __str__(self):
        return f"Reservation by {self.user} at {self.created_at}"


class Ticket(models.Model):
    row = models.IntegerField()
    seat = models.IntegerField()
    show_session = models.ForeignKey(ShowSession, on_delete=models.CASCADE, related_name="tickets")
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name="tickets")

    def __str__(self):
        return f"Ticket {self.row}-{self.seat} for {self.show_session}"
