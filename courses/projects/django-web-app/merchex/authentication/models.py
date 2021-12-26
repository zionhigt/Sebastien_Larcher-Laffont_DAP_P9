from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):

    CREATOR = 'CREATOR'
    SUBSCRIBER = 'SUBSCRIBER'

    ROLE_CHOICES = (
        (CREATOR, 'Créateur'),
        (SUBSCRIBER, 'Abonné')
    )

    image_profil = models.ImageField(verbose_name='Photo de profil', null=True, blank=True)
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Rôle')