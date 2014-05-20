from django import template

register = template.Library()


@register.filter(name="index")
def index(value):
    return value.id - 1
