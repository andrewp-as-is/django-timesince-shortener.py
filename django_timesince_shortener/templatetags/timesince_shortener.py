from django.template import Library
from django.utils.timesince import timesince


register = Library()


@register.filter
def timesince_shortener(d):
    if not d:
        return ''
    return timesince(d).split(',')[0]
