from django import template

from helper.helper import MiscHelper

register = template.Library()


@register.filter(name="get_range")
def get_range(value):
    helper = MiscHelper()
    #limit = [i for i in range(1, value + 1)]
    return helper.get_range(value)


@register.filter(name="get_anphabet")
def get_anphabet(value):
    helper = MiscHelper()
    return helper.get_alphabet(value)


@register.filter(name="check_in")
def check_in(value, _list):
    if value in _list:
        return True
    else:
        return False


@register.filter(name="create_tuple")
def create_tuple(r, c):
    return "%s %s" % (r, c)


@register.inclusion_tag('seat.html')
def seat_classes(booked_positions, r, c):
    booked = False
    for b_r, b_c in booked_positions:
        if b_r == r and b_c == c:
            booked = True
            break

    return {'booked': booked, 'r': r, 'c': c}
