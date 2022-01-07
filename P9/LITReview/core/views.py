from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import View
from ticket.models import Ticket
from review.models import Review
from followers.models import UserFollows
from authentication.models import User

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
            post_list = self.get_post_list(request.user)
            list_results = {
                'reviews': [item for item in post_list if item.model == "review.Review"],
                'tickets': [item for item in post_list if item.model == "ticket.Ticket"]
            }
            return render(request, 'core/posts.html', {
                'reviews': list_results["reviews"],
                'tickets': list_results["tickets"]
                })
        return redirect('login')
  
class CoreViewsHome(View):
    def get_personal_feed_list(self, user):
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

    def get_followed_feed(self, user):
        followed_users = self.get_followed_users(user)
        followed_users_ids = [user.followed_user.id for user in followed_users]
        followed_feed_tickets = Ticket.objects.filter(user__id__in=followed_users_ids)
        followed_feed_reviews = Review.objects.filter(user__id__in=followed_users_ids)
        print(followed_feed_tickets)
        return (followed_feed_reviews, followed_feed_tickets)
    
    def get_followed_users(self, user):
        followed_users = UserFollows.objects.filter(user=user)
        return followed_users

    def get_user_tickets(self, user):
        return Ticket.objects.filter(user=user)

    def get_reviews_of_tickets(self, tickets):
        return Review.objects.filter(ticket__in=tickets)

    def get_feed_list(self, user):
        reviews, tickets = self.get_followed_feed(user)
        reviews = list(reviews)
        tickets = list(tickets)
        reviews_by_user_tickets = self.get_reviews_of_tickets(self.get_user_tickets(user))
        reviews += list(reviews_by_user_tickets)
        for t in tickets:
            t.model = 'ticket.Ticket'

        for r in reviews:
            r.model = 'review.Review'
        list_results_full = reviews + tickets + list(self.get_personal_feed_list(user))
        list_results = []
        for result in list_results_full:
            if result not in list_results:
                list_results.append(result)
        return sorted(list_results, key=lambda x: x.time_created, reverse=True)

    def get(self, request):
        if not request.user.is_anonymous :
            user = User.objects.get(id=request.user.id)
            list_results = self.get_feed_list(user)
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
