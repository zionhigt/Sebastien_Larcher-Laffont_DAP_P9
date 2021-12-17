from django.http import HttpResponse
from django.shortcuts import render

from listings.models import Listing, Band

from listings.forms import ContactUsForm
from django.core.mail import send_mail

from django.shortcuts import redirect

# Create your views here.
def hello():
    return HttpResponse('<h1>Hello Django !</h1>')

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')

def annoncement(request, id):
    annonce = Listing.objects.get(id=id)
    return render(request, 'listings/annonce.html', {
        'annonce': annonce
    })


def annoncements(request):
    annonces = Listing.objects.all()
    return render(request, 'listings/annonces.html', {
        'annonces': annonces,
        'id': id
    })

def bands(request):
    bands = Band.objects.all()
    return render(request, 'listings/bands.html', {
        'bands': bands
    })

def contact(request):
    if request.method == 'POST':
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
    return render(request, 'listings/contact.html', {
        'form': form
    })

def email_sent(request):
    return render(request, 'listings/email-sent.html')
