from django.shortcuts import (
    render, get_object_or_404, redirect, render_to_response
)
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.template import RequestContext
#from django.http import HttpResponse
import json

from helper.helper import MovieHelper, ScheduleHelper, CinemaRoomHelper
from movie.models import Version
from ticket.models import Schedule, TicketType, Ticket
from reservation.models import Reservation
from facility.models import MovieTheater


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


def ajax_seats(request):
    if request.is_ajax():
        #helper = CinemaRoomHelper()
        schedule = Schedule.objects.get(
            pk=request.GET.get('schedule_id', None))

        # Get customer tickets
        tickets = json.loads(request.GET.get('tickets', None))

        booked_tickets = Ticket.objects.filter(
            reservation__isnull=True,
            schedule=schedule,
        )
        print booked_tickets

        for key in tickets:
            type_id = tickets[key]['id']
            tickets[key]['object'] = TicketType.objects.get(pk=type_id)

        return render_to_response(
            'choice-seats.html',
            {'tickets': tickets, 'schedule': schedule,
                'booked_tickets': booked_tickets},
            context_instance=RequestContext(request)
        )


def select_schedules(request):
    helper = MovieHelper()
    available_movies = helper.get_current()
    return render(request, 'select-schedule.html', {
        "movies": available_movies
    })


def ajax_theaters(request):
    if request.is_ajax():
        movie_id = request.GET.get('movie_id', None)
        movie = Version.objects.get(pk=movie_id)
        theaters = movie.available_theaters.all()
        return render_to_response(
            'show-available-theaters.html',
            {'theaters': theaters},
            context_instance=RequestContext(request)
        )


def ajax_schedules(request):
    if request.is_ajax():
        helper = ScheduleHelper()
        movie = Version.objects.get(pk=request.GET.get('movie_id', None))

        theater = MovieTheater.objects.get(
            pk=request.GET.get('theater_id', None))

        schedules = helper.get_schedules_by_theater(
            movie=movie, theater=theater)

        return render_to_response(
            'show-available-schedules.html',
            {'schedules': schedules},
            context_instance=RequestContext(request)
        )
