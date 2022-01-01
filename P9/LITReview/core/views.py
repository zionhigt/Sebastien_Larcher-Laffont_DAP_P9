from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import View
from ticket.models import Ticket
from review.models import Review

# Create your views here.
class CoreViewsHome(View):
    def get(self, request):
        if not request.user.is_anonymous :
            tickets = Ticket.objects.all()
            reviews = Review.objects.all()
            return render(request, 'core/home.html', {'reviews': reviews, 'tickets': tickets})
        return redirect('login')

class CoreViewsContact(View):
    def post(self, request):
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us Form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['me@dev.com']
            )
            return redirect('email-sent')
        else:
            form = ContactUsForm()
            return render(request, 'core/contact.html', {
                'form': form
            })
    
    def get(self, request):
        form = ContactUsForm()
        return render(request, 'core/contact.html', {
            'form': form
        })

class CoreViewsEmailSent(View):
    def get(self, request):
        return render(request, 'core/email-sent.html')
