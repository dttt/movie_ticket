from django import template

register = template.Library()


@register.filter(name="limit")
def limit(value):
    limit = [i for i in range(1, value + 1)]
    return limit
