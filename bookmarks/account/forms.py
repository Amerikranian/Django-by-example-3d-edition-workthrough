from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    """Form used for user login
    Attributes:
      username (CharField): The username of the user
      password (CharField): The password of the user
    """

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    """A form used for user registration
    Attributes:
      password (CharField): The desired password of the registered individual
      password2 (CharField): The repetition of the desired password
    Methods:
      clean_password2: Used for ensuring that the two provided passwords match.
    """

    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "first_name", "email")

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Passwords do not match.")
        return cd["password2"]
