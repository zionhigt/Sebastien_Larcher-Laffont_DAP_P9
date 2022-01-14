from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    image_profil = models.ImageField(
        verbose_name='Image du profil',
        upload_to='images/profils/',
        null=True, blank=True, help_text="Max: 2mo"
    )
