from django.shortcuts import render

from helper.misc import get_loop_time
from facility.models import New


def home(request):
    news = New.objects.all()[:5]
    loop_times = get_loop_time(news)
    return render(
        request,
        'home.html',
        {"news": news, "loop_times": loop_times}
    )
