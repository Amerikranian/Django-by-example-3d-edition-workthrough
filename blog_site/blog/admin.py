from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Attributes displayed on the post page
    list_display = ("title", "slug", "author", "publish", "status")
    # Attribute filters
    list_filter = ("status", "created", "publish", "author")
    # Fields to be searched
    search_fields = ("title", "body")
    # Fields which will fill out automatically as you fill out their tuple specifications
    prepopulated_fields = {"slug": ("title",)}
    # Ability to enter ids instead of having to scroll through a dropdown menu
    raw_id_fields = ("author",)
    # Navigation by published date
    date_hierarchy = "publish"
    # Controls in what order posts will be displayed on the model page
    ordering = ("status", "publish")
