from django.shortcuts import render, redirect
from django.conf import settings
from authentication.forms import SignupForm
from attachments.forms import ImageProfilForm
from django.contrib.auth import login, logout, authenticate
from authentication.models import User
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
    user_form_class = SignupForm
    image_form_class = ImageProfilForm

    def get(self, request):
        user_form = self.user_form_class()
        image_form = self.image_form_class()
        return render(request, self.template_name, {
            'user_form': user_form,
            'image_form': image_form,
            'message': ""
         })

    def post(self, request):
        user_form = self.user_form_class(request.POST)
        image_form = self.image_form_class(request.POST, request.FILES)
        message = ''
        if all([user_form.is_valid(), image_form.is_valid()]):
            user = user_form.save()
            login(request, user)
            image = image_form.save(commit=False)
            image.uploader = request.user
            image = image_form.save()
            logged_user  = User.objects.filter(id=request.user.id)
            logged_user.update(image_profil=image)
            return redirect(settings.LOGIN_REDIRECT_URL)
        message = 'Impossible de créer un compte avec les informations que vous nous avez fournis'
        return render(request, self.template_name, {
            'user_form': user_form,
            'image_form': image_form,
            'message': message
        })