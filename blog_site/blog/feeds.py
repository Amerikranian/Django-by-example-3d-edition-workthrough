from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse_lazy
from .models import Post


class LatestPostsFeed(Feed):
    """A feed for the latest blog posts
    Attributes:
      title (str): The title of the feed
      link (str): The link for the feed
      description (str): The description of the content the feed contains
    Methods:
      items: A method for fetching the latest posts in the feed
      item_title (item): Returns the title of the post, used by the items method
      item_description (item): Returns the description of the Post, used by the items method
    """

    title = "My Blog"
    link = reverse_lazy("blog:post_list")
    description = "New posts from my blog"

    def items(self):
        return Post.published.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.body, 30)
