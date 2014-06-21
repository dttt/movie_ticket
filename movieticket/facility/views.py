from django.shortcuts import render, get_object_or_404
from django.template.response import TemplateResponse

from facility.models import MovieTheater


def theaters_index(request):
    theaters = MovieTheater.objects.all()
    return render(request, 'theaters-index.html', {"theaters": theaters})


def theater_show(request, theater_slug):
    theater = get_object_or_404(MovieTheater, slug=theater_slug)
    if request.is_ajax():
        return TemplateResponse(
            request, 'theater-ajax.html', {'theater': theater})
    else:
        theaters = MovieTheater.objects.all()
        return render(request, 'theaters-index.html', {
            'theaters': theaters,
        })
