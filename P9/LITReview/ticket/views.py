from django.shortcuts import render, redirect
from django.views.generic import View
from ticket.forms import CreateTicketForm
from authentication.models import User
from ticket.models import Ticket

# Create your views here.
class CreateTicketView(View):
    form_class = CreateTicketForm

    def get(self, request):
        form = self.form_class()
        return render(request, 'ticket/create_page.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            without_user = form.save(commit=False)
            without_user.user = User.objects.get(id=request.user.id)
            without_user.save()
            return redirect('home')
        return render(request, 'ticket/create_page.html', {'form': form})

class UpdateTicketView(View):
    form_class = CreateTicketForm
    def get(self, request, id):
        ticket = Ticket.objects.get(id=id)
        if not request.user.is_anonymous:
            if request.user.id == ticket.user.id:
                form = self.form_class(instance=ticket)
                return render(request, 'ticket/update_form.html', {
                    'form': form
                })
        return redirect('login')

    def post(self, request, id):
        ticket = Ticket.objects.get(id=id)
        if not request.user.is_anonymous:
            if request.user.id == ticket.user.id:
                form = self.form_class(request.POST, instance=ticket)
                if form.is_valid():
                    form.save()
                    return redirect('post')
                return render(request, 'ticket/update_form.html', {
                    'form': form
                })
        return redirect('login')