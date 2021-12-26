from django.shortcuts import render, redirect
from django.conf import settings
from authentication.forms import SignupForm
from django.contrib.auth import login, logout, authenticate
from django.views.generic import View


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
    form_class = SignupForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form, 'message': ""})

    def post(self, request):
        form = self.form_class(request.POST)
        message = ''
        print(form['image_profil'])
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
        message = 'Impossible de créer un compte avec les informations que vous nous avez fournis'
        return render(request, self.template_name, {'form': form, 'message': message})