from django.shortcuts import render, redirect
from django.views.generic import View
from review.forms import CreateReviewForm
from ticket.forms import CreateTicketForm
from authentication.models import User
from review.models import Review
from ticket.models import Ticket

# Create your views here.
class CreateReviewView(View):
    form_class = CreateReviewForm
    ticket_form = CreateTicketForm

    def get_ticket_by_id(self, id):
        try:
            ticket = Ticket.objects.get(id=id)
            return ticket
        except Ticket.DoesNotExist:
            return None

    def get(self, request, ticket_id=None):
        if not request.user.is_anonymous:
            form = self.form_class()
            ticket_form = self.ticket_form()
            ticket= None
            if ticket_id is not None:
                review_ticket = self.get_ticket_by_id(ticket_id)
                if review_ticket is not None:
                    ticket = review_ticket
                    ticket_form = None
            return render(request, 'review/create_page.html', {'form': form, 'ticket': ticket, 'ticket_form': ticket_form})
        return redirect('login')

    def post(self, request, ticket_id=None):
        current_user = User.objects.get(id=request.user.id)
        if not request.user.is_anonymous:
            form = self.form_class(request.POST)
            if form.is_valid():
                without_user = form.save(commit=False)
                without_user.rating = int(form.cleaned_data['rating_choices'])
                without_user.user = current_user
                ticket = None
                if ticket_id:
                    ticket = self.get_ticket_by_id(ticket_id)
                    print(ticket)
                else:
                    ticket_form = self.ticket_form(request.POST, request.FILES)
                    if ticket_form.is_valid():
                        ticket = ticket_form.save(commit=False)
                        ticket.user = current_user
                if ticket:
                    without_user.ticket = ticket
                    ticket.has_review = True
                    ticket.save()
                without_user.save()
                return redirect('home')
            return render(request, 'review/create_page.html', {'form': form})
        return redirect('login')


class UpdateReviewView(View):
    form_class = CreateReviewForm
    def get(self, request, id):
        review = Review.objects.get(id=id)
        if not request.user.is_anonymous:
            if request.user.id == review.user.id:
                form = self.form_class(instance=review)
                form.fields['rating_choices'].initial = int(review.rating)
                print(form.fields['rating_choices'])
                return render(request, 'review/update_form.html', {
                    'form': form
                })
        return redirect('login')

    def post(self, request, id):
        review = Review.objects.get(id=id)
        if not request.user.is_anonymous:
            if request.user.id == review.user.id:
                form = self.form_class(request.POST, instance=review)
                if form.is_valid():
                    form_without_rating = form.save(commit=False)
                    form_without_rating.rating = int(form.cleaned_data['rating_choices'])
                    form_without_rating.save()
                    return redirect('post')
                return render(request, 'review/update_form.html', {
                    'form': form
                })
        return redirect('login')


def delete_confirm(request, id):
    review = Review.objects.get(id=id)
    if not request.user.is_anonymous:
        if request.user.id == review.user.id:
            
            return render(request, 'review/delete_confirm.html', {
                'id': id
            })
    return redirect('login')

def delete_by_id(request, id):
    review = Review.objects.get(id=id)
    print(review)
    if not request.user.is_anonymous:
        if request.user.id == review.user.id:
            review.delete()
            return redirect('post')
    return redirect('login')