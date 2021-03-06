from django import template
from products.models import Product, THUMB_CHOICES
register = template.Library()

@register.filter
def get_thumbnail(obj,arg):
    #obj == Product instance

    if not isinstance(obj,Product):
        raise TypeError('This is not a valid product model.')
    choices = dict(THUMB_CHOICES)
    if not choices.get(arg):
        raise TypeError('This is not a valid type of this model.')

    try:
        return obj.thumbnail_set.filter(type=arg).first().media.url
    except:
        return None
