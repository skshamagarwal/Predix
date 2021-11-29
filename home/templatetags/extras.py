from django import template
import random as r

register = template.Library()


@register.filter(name='split')
def split(value, key):
    return value.split(key)

@register.filter(name='random')
def random(value):
    s = value.split(',')
    return r.choice(s)