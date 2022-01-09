from django.db import models
from django.db.models import UniqueConstraint
from django.conf import settings


class UserFollows(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='following')
    followed_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='followed_by')

    class Meta:
        constraints = [
            UniqueConstraint(
                name='unique_together',
                fields=['user', 'followed_user']
            )
        ]
