from django.shortcuts import (
    render, get_object_or_404, redirect, render_to_response
)
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.template import RequestContext
from django.template.response import TemplateResponse
from django.db import transaction
#from djpjax import pjax
#from django.http import HttpResponse
import json


from helper.helper import MovieHelper, ScheduleHelper
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


@login_required
@transaction.atomic
def finish(request):
    if request.method == "POST":
        positions_json = request.POST.get('positions', None)
        schedule_id = request.POST.get('schedule_id', None)

        if positions_json and schedule_id:
            booked_tickets = []
            # Save user's selected to session for reselect
            request.session['positions'] = positions_json
            request.session['schedule_id'] = schedule_id

            # Create new reservation
            reservation = Reservation(customer=request.user)
            reservation.save()

            positions = json.loads(positions_json)
            for position in positions:
                print position[0]
                print position[1]
                ticket = Ticket.objects.get(
                    row=position[0],
                    column=position[1],
                    schedule__id=schedule_id,
                )
                ticket.reservation = reservation
                ticket.save()
                booked_tickets.append(ticket)

            return render(request, 'final-step.html', {
                'booked_tickets': booked_tickets,
                'schedule': Schedule.objects.get(pk=schedule_id),
                }
            )


def ajax_seats(request):
    if request.is_ajax():
        schedule_id_input = request.POST.get('schedule_id', None)
        tickets_input = request.POST.get('tickets', None)

        if schedule_id_input and tickets_input:
            schedule = Schedule.objects.get(pk=schedule_id_input)
            tickets = json.loads(tickets_input)

            booked_tickets = Ticket.objects.filter(
                reservation__isnull=False,
                schedule=schedule,
            )

            booked_positions = [
                (ticket.row, ticket.column) for ticket in booked_tickets]

            for key in tickets:
                type_id = tickets[key]['id']
                tickets[key]['object'] = TicketType.objects.get(pk=type_id)

            return TemplateResponse(request, 'choice-seats.html', {
                'tickets': tickets,
                'schedule': schedule,
                'booked_positions': booked_positions},
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


def ajax_finish(request):
    pass
