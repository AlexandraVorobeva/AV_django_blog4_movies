from django import template
from general.models import Category, Movie

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()

@register.inclusion_tag('general/tags/last_movies.html')
def get_last_movies():
    movies = Movie.objects.order_by("id")[:2]
    return {'last_movies': movies}
