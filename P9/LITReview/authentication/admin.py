from django.contrib import admin
from authentication.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'role', 'password')

admin.site.register(User, UserAdmin)
# Register your models here.