from django import template
from ..models import Post

register = template.Library()


@register.simple_tag
def total_posts():
    """Returns the number of total posts on the site"""
    return Post.published.count()
