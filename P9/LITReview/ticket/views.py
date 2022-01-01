from django.shortcuts import render, redirect
from django.views.generic import View
from ticket.forms import CreateTicketForm
from authentication.models import User

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
