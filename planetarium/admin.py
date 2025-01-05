from django.contrib import admin

from planetarium.models import (
    ShowSession,
    ShowTheme,
    Reservation,
    AstronomyShow,
    PlanetariumDome,
    Ticket,
)

admin.site.register(ShowSession)
admin.site.register(ShowTheme)
admin.site.register(Ticket)
admin.site.register(Reservation)
admin.site.register(PlanetariumDome)
admin.site.register(AstronomyShow)
