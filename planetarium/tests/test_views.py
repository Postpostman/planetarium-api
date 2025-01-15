from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .factories import (
    AstronomyShowFactory,
    ShowThemeFactory,
    PlanetariumDomeFactory,
    ShowSessionFactory,
    ReservationFactory,
    TicketFactory,
)
from planetarium.models import AstronomyShow, ShowTheme, PlanetariumDome, ShowSession, Reservation, Ticket


class AstronomyShowViewSetTest(APITestCase):
    def setUp(self):
        self.show = AstronomyShowFactory()
        self.url = reverse("planetarium:astronomyshow-list")

    def test_list_astronomy_shows(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_astronomy_show(self):
        data = {"name": "Starry Nights"}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(AstronomyShow.objects.count(), 2)


class ShowThemeViewSetTest(APITestCase):
    def setUp(self):
        self.theme = ShowThemeFactory()
        self.url = reverse("planetarium:showtheme-list")

    def test_list_show_themes(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_show_theme(self):
        data = {"name": "Cosmic Wonders"}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ShowTheme.objects.count(), 2)


class PlanetariumDomeViewSetTest(APITestCase):
    def setUp(self):
        self.dome = PlanetariumDomeFactory()
        self.url = reverse("planetarium:planetariumdome-list")

    def test_list_planetarium_domes(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_planetarium_dome(self):
        data = {"name": "Secondary Dome"}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PlanetariumDome.objects.count(), 2)


class ShowSessionViewSetTest(APITestCase):
    def setUp(self):
        self.session = ShowSessionFactory()
        self.url = reverse("planetarium:showsession-list")

    def test_list_show_sessions(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_show_session(self):
        data = {"title": "Evening Show"}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ShowSession.objects.count(), 2)


class ReservationViewSetTest(APITestCase):
    def setUp(self):
        self.reservation = ReservationFactory()
        self.url = reverse("planetarium:reservation-list")

    def test_list_reservations(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_reservation(self):
        data = {"name": "Jane Doe"}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Reservation.objects.count(), 2)


class TicketViewSetTest(APITestCase):
    def setUp(self):
        self.ticket = TicketFactory()
        self.url = reverse("planetarium:ticket-list")

    def test_list_tickets(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_ticket(self):
        data = {"number": "54321"}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Ticket.objects.count(), 2)
