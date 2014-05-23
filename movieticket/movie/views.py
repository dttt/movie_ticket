from django.shortcuts import render, get_object_or_404

from news.models import New
from helper.helper import MovieHelper
from movie.models import Movie, Version


def home(request):
    helper = MovieHelper()
    news = New.objects.all()[:5]
    current_movies = helper.get_current(limit=5)
    future_movies = helper.get_future(limit=5)
    available_movies = helper.get_current()

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
    version = get_object_or_404(Version, slug=version_slug)
    return render(request, 'show-version.html', {"version": version})
