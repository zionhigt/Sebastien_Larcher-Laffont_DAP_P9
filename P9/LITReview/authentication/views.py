from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import login, logout, authenticate
from django.views.generic import View

from authentication.forms import SignupForm
from authentication.models import User

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

class AccountView(View):
    def get(self, request):
        if not request.user.is_anonymous:
            return render(request, 'authentication/user_page.html', {'user': request.user})
        return redirect('login')

class SignupView(View):
    template_name = 'authentication/signup_page.html'
    user_form_class = SignupForm

    def get(self, request):
        user_form = self.user_form_class()
        return render(request, self.template_name, {
            'user_form': user_form,
            'message': ""
         })

    def post(self, request):
        user_form = self.user_form_class(request.POST, request.FILES)
        message = ''
        if user_form.is_valid():
            user = user_form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
        message = 'Impossible de créer un compte avec les informations que vous nous avez fournis'
        return render(request, self.template_name, {
            'user_form': user_form,
            'message': message
        })