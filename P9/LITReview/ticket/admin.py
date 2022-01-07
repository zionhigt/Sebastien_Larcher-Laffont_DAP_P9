from django.contrib import admin
from ticket.models import Ticket

class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')

admin.site.register(Ticket, TicketAdmin)
# Register your models here.