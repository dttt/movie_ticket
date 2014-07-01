from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.template.response import TemplateResponse

from news.models import New
from helper.helper import MovieHelper, ScheduleHelper
from movie.models import Movie, Version


def home(request):
    helper = MovieHelper()
    news = New.objects.all()[:5]
    current_movies_list = helper.get_current()
    future_movies_list = helper.get_future()
    available_movies = helper.get_current()

    c_paginator = Paginator(current_movies_list, 3)
    f_paginator = Paginator(future_movies_list, 3)

    current_movies = c_paginator.page(1)
    future_movies = f_paginator.page(1)

    if request.is_ajax():
        container = request.GET.get('container')
        query = request.GET.get('query')
        page = request.GET.get('page')

        print page
        print query
        print container

        if query == 'c_page':
            movies = helper.get_page(c_paginator, page)
        else:
            movies = helper.get_page(f_paginator, page)

        return TemplateResponse(request, 'list-movies.html', {
            'movies': movies,
            'container': container,
            'query': query,
            }
        )

    return render(request, 'home.html', {
        "news": news,
        'current_movies': current_movies,
        'future_movies': future_movies,
        'available_movies': available_movies,
        }
    )


def show_movie(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'show-movie.html', {"movie": movie})


def show_version(request, version_slug):
    helper = ScheduleHelper()

    version = get_object_or_404(Version, slug=version_slug)
    schedules = helper.get_sorted_schedules(movie=version)

    return render(request, 'show-version.html', {
        "version": version,
        "sorted_schedules": schedules,
    })
