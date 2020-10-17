from django import forms


class LoginForm(forms.Form):
    """Form used for user login
    Attributes:
      username (CharField): The username of the user
      password (CharField): The password of the user
    """

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
