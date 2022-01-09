from django import forms
from ticket.models import Ticket


class CreateTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('title', 'description', 'image')
