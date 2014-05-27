from django.contrib import admin
from .models import Schedule, TicketType, Ticket


admin.site.register(Schedule)
admin.site.register(TicketType)
admin.site.register(Ticket)
