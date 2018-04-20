from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def uppa(value):
    return value.upper()


@register.filter(name='first_words')
@stringfilter
def first_words(value):
    return ' '.join(value.split()[:20])


@register.filter(name='last_words')
@stringfilter
def last_words(value):
    return ' '.join(value.split()[20:])