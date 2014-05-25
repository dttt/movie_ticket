from django.shortcuts import render, get_object_or_404

from news.models import New


def show(request, new_slug):
    new = get_object_or_404(New, slug=new_slug)
    return render(request, 'new.html', {"new": new})
