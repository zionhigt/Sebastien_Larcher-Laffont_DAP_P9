from django.contrib import admin
from followers.models import UserFollows


class UserFollowsAdmin(admin.ModelAdmin):
    list_display = ('user', 'followed_user')


admin.site.register(UserFollows, UserFollowsAdmin)
