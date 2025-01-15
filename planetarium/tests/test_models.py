from django.test import TestCase
from planetarium.models import AstronomyShow, PlanetariumDome, Reservation, ShowSession, ShowTheme, Ticket
from planetarium.tests.factories import (
    UserFactory,
    AstronomyShowFactory,
    PlanetariumDomeFactory,
    ReservationFactory,
    ShowThemeFactory,
    ShowSessionFactory,
    TicketFactory,
)


class IsStr(TestCase):
    def setUp(self):
        self.user = UserFactory(email="testuser@gmail.com")
        self.astronomy_show = AstronomyShowFactory(title="Planets of Sun System")
        self.planetarium_dome = PlanetariumDomeFactory(name="Main Dome")
        self.reservation = ReservationFactory(user=self.user)
        self.show_theme = ShowThemeFactory(name="Space Exploration")
        self.show_session = ShowSessionFactory(
            astronomy_show=self.astronomy_show,
            planetarium_dome=self.planetarium_dome,
            show_time="2024-01-13 12:00",
        )
        self.ticket = TicketFactory(
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
