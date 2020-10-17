from django.contrib.sitemaps import Sitemap
from .models import Post


class PostSitemap(Sitemap):
    """The sitemap for the Posts model"""

    changefreq = "weekly"
    priority = 0.9

    def items(self):
        """Returns all of the published posts"""
        return Post.published.all()

    def lastmod(self, obj):
        """Receives each object from the items method and returns their last modification date"""
        return obj.updated
