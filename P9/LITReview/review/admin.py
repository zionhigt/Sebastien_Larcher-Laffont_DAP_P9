from django.contrib import admin
from review.models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('headline', 'ticket')


admin.site.register(Review, ReviewAdmin)
