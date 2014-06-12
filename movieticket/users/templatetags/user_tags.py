from django import template


register = template.Library()


@register.filter(name="get_movie")
def get_movie(value):
    return value.schedule.movie
