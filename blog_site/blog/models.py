from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager


class PublishedManager(models.Manager):
    """A simple manager used to sort posts by their status"""

    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status="published")


class Post(models.Model):
    """A model representing blog posts
    Attributes:
      STATUS_CHOICES (tuple): Post status options
      title (CharField, length<=250): The title of the post
      slug (CharField, length<=250): Used for URL purposes
      author (ForeignKey to User): The author of the post. Users can access the Post model via 'blog_posts' attribute
      body (TextField): The contents of the post
      publish (DateTimeField): The date during which the post was published (status, not date)
      created (DateTimeField): The date during which the post was made
      updated (DateTimeField): The date during which the last update to the post was made
      status (CharField): The current status of the post, limitted to STATUS_CHOICES
      objects (Manager): The default models.Manager object
      published (PublishedManager): Custom object manager which sorts posts by post's status, excluding drafts
      tags (TaggableManager): A list of tags associated with the post
    Methods:
      get_absolute_url: Constructs and returns a url for the current post
    """

    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published", "Published"),
    )
    title = models.CharField(max_length=250)
    slug = models.CharField(max_length=250, unique_for_date="publish")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    # Note: auto_now_add causes date to be added upon object creation.
    # auto_now will cause the date to be updated every time an object is saved
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")
    # We have to explicitly add the objects attribute because we create a custom manager for the model
    objects = models.Manager()
    published = PublishedManager()
    tags = TaggableManager()

    class Meta:
        ordering = ("-publish",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "blog:post_detail",
            args=[self.publish.year, self.publish.month, self.publish.day, self.slug],
        )


class Comment(models.Model):
    """A model representing comments made by users on posts
    Attributes:
      post (ForeignKey to Post): The post on which the comment was made
      name (CharField): The name of the user who commented on the post
      email (EmailField): The email address of the user who made the comment concerning the post
      body (TextField): The contents of the comment
      create (DateTimeField): The date during which the comment was made
      updated (DateTimeField): The date during which the comment was edited
      active (BooleanField): Determines if the comment is visible on the page
    """

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ("created",)

    def __str__(self):
        return f"Comment by {self.name} ({self.email}) on {self.post}"
