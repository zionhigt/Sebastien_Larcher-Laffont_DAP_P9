from django.db import models
from django.conf import settings


class Ticket(models.Model):
    title = models.CharField(verbose_name="Titre", max_length=128)
    description = models.TextField(verbose_name="Description", max_length=2048, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Image', upload_to='images/tickets/', null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    has_review = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}"
