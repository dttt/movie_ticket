from django.shortcuts import render

from facility.models import MovieTheater


def theaters_index(request):
    theaters = MovieTheater.objects.all()
    return render(request, 'theaters-index.html', {"theaters": theaters})


def theater_show(request, facility_id):
    theater = MovieTheater.objects.get(pk=facility_id)
