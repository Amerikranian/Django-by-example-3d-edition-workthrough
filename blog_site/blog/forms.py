from django import forms
from .models import Comment


class EmailPostForm(forms.Form):
    """A form used for sending emails
    Attributes:
      name (CharField<=25): The name of the sender
      email (EmailField): The address of the sender
      to (EmailField): The address of the recipient
      comments (CharField, optional): Comments about the shared item
    """

    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    """A form representing the posting of a new comment upon a post"""

    class Meta:
        model = Comment
        # Fields shown in the form
        # We exclude active and the dates because those will be automatically set by the object as it saves
        fields = ("name", "email", "body")
