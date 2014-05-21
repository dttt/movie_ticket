from django.shortcuts import render

from facility.models import MovieTheater


def theaterIndex(request):
    theaters = MovieTheater.objects.all()
    return render(request, 'theaters.html', {"theaters": theaters})
