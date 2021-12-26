from django.http import HttpResponse
from django.shortcuts import render

from listings.models import Listing, Band

from listings.forms import ContactUsForm
from django.core.mail import send_mail

from django.shortcuts import redirect

from listings.forms import AddBandForm
from listings.forms import AddAnnoncementForm

# Create your views here.
def hello():
    return HttpResponse('<h1>Hello Django !</h1>')

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')

def bands(request):
    bands = Band.objects.all()
    return render(request, 'listings/bands.html', {
        'bands': bands
    })

def band(request, id):
    print(request.keys())
    band = Band.objects.get(id=id)
    return render(request, 'listings/band.html', {
        'band': band
    })

def addBand(request):
    if request.method == 'POST':
        form = AddBandForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect('unique-band', band.id)
    else:
        form = AddBandForm()

    return render(request, 'listings/band_add.html', {'form': form})

def updateBand(request, id):
    band = Band.objects.get(id=id)
    if request.method == 'POST':
        form = AddBandForm(request.POST, instance=band)
        if form.is_valid():
            band = form.save()
            return redirect('unique-band', band.id)
    else:
        form = AddBandForm(instance=band)

    return render(request, 'listings/band_update.html', {'form': form})

def deleteBand(request, id):
    band = Band.objects.get(id=id)
    if request.method == 'POST':
        band.delete()
        return redirect('bands')

    return render(request, 'listings/band_delete_confirm.html', {'band': band})

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

def addAnnoncement(request):
    if request.method == 'POST':
        form = AddAnnoncementForm(request.POST)
        if form.is_valid():
            annoncement = form.save()
            return redirect('unique-annonce', annoncement.id)
    else:
        form = AddAnnoncementForm()

    return render(request, 'listings/annoncement_add.html', {'form': form})

def updateAnnoncement(request, id):
    annoncement = Listing.objects.get(id=id)
    if request.method == 'POST':
        form = AddAnnoncementForm(request.POST, instance=annoncement)
        if form.is_valid():
            annoncement = form.save()
            return redirect('unique-annonce', annoncement.id)
    else:
        form = AddAnnoncementForm(instance=annoncement)

    return render(request, 'listings/annoncement_update.html', {'form': form})

def deleteAnnoncement(request, id):
    annoncement = Listing.objects.get(id=id)
    if request.method == 'POST':
        annoncement.delete()
        return redirect('annonces')
    
    return render(request, 'listings/annoncement_delete_confirm.html', {'annonce': annoncement})

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
