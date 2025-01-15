import factory
from django.contrib.auth import get_user_model
from planetarium.models import (
    AstronomyShow,
    PlanetariumDome,
    Reservation,
    ShowSession,
    ShowTheme,
    Ticket,
)

User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Faker("email")
    password = factory.PostGenerationMethodCall("set_password", "testpass")


class AstronomyShowFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AstronomyShow

    title = "Planets of Sun System"
    description = "Explore your Galactic"


class PlanetariumDomeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PlanetariumDome

    name = "Main Dome"
    rows = 10
    seats_in_row = 20


class ReservationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Reservation

    user = factory.SubFactory(UserFactory)


class ShowThemeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ShowTheme

    name = "Space Exploration"


class ShowSessionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ShowSession

    astronomy_show = factory.SubFactory(AstronomyShowFactory)
    planetarium_dome = factory.SubFactory(PlanetariumDomeFactory)
    show_time = "2024-01-13 12:00"


class TicketFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ticket

    row = 1
    seat = 1
    show_session = factory.SubFactory(ShowSessionFactory)
    reservation = factory.SubFactory(ReservationFactory)
