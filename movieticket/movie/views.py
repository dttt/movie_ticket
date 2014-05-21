from django.shortcuts import render

from helper.misc import get_loop_time
from news.models import New
from movie.models import Movie


def home(request):
    news = New.objects.all()[:5]
    loop_times = get_loop_time(news)
    return render(
        request,
        'home.html',
        {"news": news, "loop_times": loop_times}
    )


def show_movie(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'show-movie.html', {"movie": movie})
