from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import View
from ticket.models import Ticket
from review.models import Review

# Create your views here.
class CoreViewsPost(View):
    def get_post_list(self, user):
        tickets = []
        for t in Ticket.objects.filter(user=user):
            t.model = 'ticket.Ticket'
            tickets.append(t)
        reviews = []
        for r in Review.objects.filter(user=user):
            r.model = 'review.Review'
            reviews.append(r)
        records = tickets + reviews
        feed_list = sorted(records, key=lambda x: x.time_created, reverse=True)
        return feed_list

    def get(self, request):
        if not request.user.is_anonymous :
            list_results = self.get_post_list(request.user)
            return render(request, 'core/home.html', {'list_results': list_results})
        return redirect('login')


class CoreViewsHome(View):
    def get_personal_feed_list(self, user):
        tickets = []
        for t in Ticket.objects.get(user=user):
            t.model = 'ticket.Ticket'
            tickets.append(t)
        reviews = []
        for r in Review.objects.get(user=user):
            r.model = 'review.Review'
            reviews.append(r)
        records = tickets + reviews
        feed_list = sorted(records, key=lambda x: x.time_created, reverse=True)
        return feed_list
    def get_feed_list(self):
        tickets = []
        for t in Ticket.objects.all():
            t.model = 'ticket.Ticket'
            tickets.append(t)
        reviews = []
        for r in Review.objects.all():
            r.model = 'review.Review'
            reviews.append(r)
        records = tickets + reviews
        feed_list = sorted(records, key=lambda x: x.time_created, reverse=True)
        return feed_list

    def get(self, request):
        if not request.user.is_anonymous :
            list_results = self.get_feed_list()
            return render(request, 'core/home.html', {'list_results': list_results})
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
