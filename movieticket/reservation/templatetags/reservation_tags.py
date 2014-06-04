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
