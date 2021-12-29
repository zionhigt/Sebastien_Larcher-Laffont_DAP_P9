from django.db import models
from django.conf import settings

# Create your models here.
class Image(models.Model):
    caption = models.CharField(max_length=120, blank=True)
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

class ImageProfil(Image):
    location = 'images/profils/'
    image = models.ImageField(verbose_name='Image', upload_to=location)

class ImageTicket(Image):
    location = 'images/tickets/'
    image = models.ImageField(verbose_name='Image', upload_to=location)