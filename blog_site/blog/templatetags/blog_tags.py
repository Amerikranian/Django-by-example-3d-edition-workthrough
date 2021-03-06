from django import template
from django.db.models import Count
from django.utils.safestring import mark_safe
from ..models import Post
import markdown

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


@register.simple_tag
def get_most_commented_posts(count=5):
    """Retrieves the specified number of posts, ordered by the number of comments they recieved
    Parameters:
        count (int): The number of posts to return
    """
    return Post.published.annotate(total_comments=Count("comments")).order_by(
        "-total_comments", "-publish"
    )


@register.filter(name="markdown")
def markdown_format(text):
    """Applies the markdown format to the given text
    Parameters:
        text (str): The text to be processed
    Return Value:
        A converted string of markdown text
    """
    return mark_safe(markdown.markdown(text))
