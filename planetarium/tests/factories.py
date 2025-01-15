import factory

from planetarium.models import (
    AstronomyShow,
    ShowTheme,
    PlanetariumDome,
    ShowSession,
    Reservation,
    Ticket,
)


class AstronomyShowFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AstronomyShow

    name = "Galactic Adventures"


class ShowThemeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ShowTheme

    name = "Space Exploration"


class PlanetariumDomeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PlanetariumDome

    name = "Main Dome"


class ShowSessionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ShowSession

    title = "Morning Show"


class ReservationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Reservation

    name = "John Doe"


class TicketFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ticket

    number = "12345"
