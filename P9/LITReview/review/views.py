from django.shortcuts import render, redirect
from django.views.generic import View
from review.forms import CreateReviewForm
from authentication.models import User

# Create your views here.
class CreateReviewView(View):
    form_class = CreateReviewForm

    def get(self, request):
        form = self.form_class()
        return render(request, 'review/create_page.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            without_user = form.save(commit=False)
            without_user.user = User.objects.get(id=request.user.id)
            without_user.save()
            return redirect('home')
        return render(request, 'review/create_page.html', {'form': form})
