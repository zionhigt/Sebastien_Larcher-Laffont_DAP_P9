from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    image_profil = models.ImageField(verbose_name='Image profil', upload_to='images/profils/', null=True, blank=True, help_text="Max: 2mo")