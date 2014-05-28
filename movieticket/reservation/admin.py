from django.contrib import admin

from .models import Reservation
from ticket.models import Ticket


class TicketInline(admin.StackedInline):
    model = Ticket


class ReservationAdmin(admin.ModelAdmin):
    inlines = [TicketInline, ]

admin.site.register(Reservation, ReservationAdmin)
