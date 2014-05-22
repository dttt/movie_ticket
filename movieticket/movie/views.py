from django.shortcuts import render, get_object_or_404

from news.models import New
from helper.helper import MovieHelper
from movie.models import Movie, Version


def home(request):
    helper = MovieHelper()
    news = New.objects.all()[:5]
    current_movies = helper.get_current()  # Version.objects.all()

    return render(
        request,
        'home.html',
        {"news": news, 'current_movies': current_movies}
    )


def show_movie(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'show-movie.html', {"movie": movie})


def show_version(request, version_slug):
    version = get_object_or_404(Version, slug=version_slug)
    return render(request, 'show-version.html', {"version": version})
