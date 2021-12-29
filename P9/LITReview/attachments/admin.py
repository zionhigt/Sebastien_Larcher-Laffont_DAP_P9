from django.contrib import admin
from attachments.models import ImageProfil

class ImageProfilAdmin(admin.ModelAdmin):
    list_display = ('image', 'caption', 'uploader', 'date_created')

admin.site.register(ImageProfil, ImageProfilAdmin)
# Register your models here.