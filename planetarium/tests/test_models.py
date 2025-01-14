from django.contrib.auth import get_user_model
from django.test import TestCase

from planetarium.models import (
    AstronomyShow,
    PlanetariumDome,
    Reservation,
    ShowSession,
    ShowTheme,
    Ticket,
)

User = get_user_model()


class IsStr(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="testuser@gmail.com", password="testpass"
        )

        self.astronomy_show = AstronomyShow.objects.create(
            title="Planets of Sun System",
            description="Explore your Galactic",
        )
        self.planetarium_dome = PlanetariumDome.objects.create(
            name="Main Dome", rows=10, seats_in_row=20
        )
        self.reservation = Reservation.objects.create(user=self.user)
        self.show_theme = ShowTheme.objects.create(name="Space Exploration")
        self.show_session = ShowSession.objects.create(
            astronomy_show=self.astronomy_show,
            planetarium_dome=self.planetarium_dome,
            show_time="2024-01-13 12:00",
        )
        self.ticket = Ticket.objects.create(
            row=1, seat=1, show_session=self.show_session, reservation=self.reservation
        )

    def test_astronomy_show_str(self):
        self.assertEqual(str(self.astronomy_show), "Planets of Sun System")

    def test_planetarium_dome_str(self):
        self.assertEqual(str(self.planetarium_dome), "Main Dome")

    def test_reservation_str(self):
        self.assertEqual(str(self.reservation), f"Reserved by {self.user}")

    def test_show_theme_str(self):
        self.assertEqual(str(self.show_theme), "Space Exploration")

    def test_show_session_str(self):
        self.assertEqual(
            str(self.show_session), "Planets of Sun System at 2024-01-13 12:00"
        )

    def test_ticket_str(self):
        self.assertEqual(
            str(self.ticket),
            "Row: 1, "
            "Seat: 1, ShowSession: "
            "Planets of Sun System at 2024-01-13 12:00",
        )
