from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.db.models import Count
from .models import Post, Comment
from .forms import EmailPostForm, CommentForm
from taggit.models import Tag


class PostListView(ListView):
    """A view for listing blog posts
    Attributes:
      queryset (Post.published.all): A queryset of objects being passed to the template
      context_object_name (str): The name which the object will be known by in the template
      paginate_by (int): Number of posts per page
      template_name (str): The name of the template used for rendering html
    """

    queryset = Post.published.all()
    context_object_name = "posts"
    paginate_by = 3
    template_name = "blog/post/list.html"


# Note: Unless stated otherwise, request is the default function argument, i.e, gets passed to everything inside the views.
# As such, when documenting parameters, request will be left out unless it will receive specific treatment
# Also, unless otherwise specified, the methods will return a render request with a specific template


def post_list(request, tag_slug=None):
    """Displays the list of posts, splitting them into pages"""
    object_list = Post.published.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug__iexact=tag_slug)
        # Filter the objects by the provided tag
        object_list = object_list.filter(tags__in=[tag])
    # We want 3 posts per page
    paginator = Paginator(object_list, 3)
    page = request.GET.get("page")
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver the last page of posts
        posts = paginator.page(paginator.num_pages)
    return render(
        request, "blog/post/list.html", {"page": page, "posts": posts, "tag": tag}
    )


def post_detail(request, year, month, day, post):
    """Attempts to display the post with the given parameters
    Parameters:
      year (int): The year during which the post was published
      month (int): The month during which the post was published
      day (int): The day during which the post was published
      slug (str): The slug of the specified post
    Note: The post must have its status set to 'published' in order to be displayed
    """
    post = get_object_or_404(
        Post,
        slug=post,
        status="published",
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Don't save to database yet, need to update the post attribute of the comment
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    # Similar posts
    # Get all the id values for the tags for the post.
    # Flat makes the values_list return [1, 2, 3] rather than [(1, ), (2, ), (3, )]
    post_tag_ids = post.tags.values_list("id", flat=True)
    # Filter the posts for similar tags, excluding the current post
    similar_posts = Post.published.filter(tags__in=post_tag_ids).exclude(id=post.id)
    # Annotate similar posts with the counts of tags, sorting them in descending order by count and published date.
    similar_posts = similar_posts.annotate(same_tags=Count("tags")).order_by(
        "-same_tags", "-publish"
    )[:4]
    return render(
        request,
        "blog/post/detail.html",
        {
            "post": post,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
            "similar_posts": similar_posts,
        },
    )


def post_share(request, post_id):
    """Allows the user to share the post by email
    Parameters:
      post_id (int): The id of the post
    Please note: The post must have the status of 'published' in order to be eligible for sharing
    """
    post = get_object_or_404(Post, id=post_id, status="published")
    sent = False
    if request.method == "POST":
        # Form was submited
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Forms passed validation
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} ({cd['email']}) recommends you read {post.title}"
            message = f"Read {post.title} at {post_url}"
            if cd["comments"]:
                message += f"\n\n{cd['name']}'s comments: {cd['comments']}"
            send_mail(subject, message, "example@gmail.com", (cd["to"],))
            sent = True
    else:
        form = EmailPostForm()
    return render(
        request, "blog/post/share.html", {"post": post, "form": form, "sent": sent}
    )
