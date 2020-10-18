from django.db import models
from django.conf import settings


class Profile(models.Model):
    """A profile for the User object
    Attributes:
      user (OneToOneField): The object to which this profile relates to
      date_of_birth (DateField): The date of birth possessed by the user
      photo (ImageField): A visual representation of how the user looks like
    """

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to="users/%Y/%m/%d/", blank=True)

    def __str__(self):
        return f"Profile for {self.user.username}"
