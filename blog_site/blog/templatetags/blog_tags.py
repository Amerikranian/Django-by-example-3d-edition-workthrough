from django import template
from ..models import Post

register = template.Library()


@register.simple_tag
def total_posts():
    """Returns the number of total posts on the site"""
    return Post.published.count()


@register.inclusion_tag("blog/post/latest_posts.html")
def show_latest_posts(count=5):
    """Shows the most recent posts
    Parameters:
        count (int): The amount of posts to show
    """
    latest_posts = Post.published.order_by("-publish")[:count]
    return {"latest_posts": latest_posts}
