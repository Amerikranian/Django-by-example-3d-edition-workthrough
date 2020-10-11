from django import forms


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
