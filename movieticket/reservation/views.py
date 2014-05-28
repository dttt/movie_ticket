from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.http import HttpResponse

from helper.helper import MovieHelper
from ticket.models import Schedule, TicketType
from reservation.models import Reservation


@login_required
def show(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)

    # Check user is valid
    if reservation.customer != request.user:
        messages.add_message(request, messages.INFO, 'Permission denied')
        return redirect(reverse('home'))

    return render(request, 'show.html', {'reservation': reservation})


@login_required
def make(request, schedule_id):
    schedule = get_object_or_404(Schedule, pk=schedule_id)
    ticket_types = TicketType.objects.all()

    return render(request, 'make-reservation.html', {
        'schedule': schedule,
        'ticket_types': ticket_types,
    })


@login_required
def select_tickets(request, schedule_id, quantity):
    pass


def select_schedules(request):
    helper = MovieHelper()
    available_movies = helper.get_current()
    return render(request, 'select-schedules.html', {
        "movies": available_movies
    })


def ajax_theaters(request):
    if request.is_ajax():
        print "It working, it working"
        return HttpResponse("You did it!")


def ajax_schedules(request):
    pass
