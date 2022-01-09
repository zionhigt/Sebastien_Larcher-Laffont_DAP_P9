from django.contrib import admin
from authentication.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'image_profil')


admin.site.register(User, UserAdmin)
