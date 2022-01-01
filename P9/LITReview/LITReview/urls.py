"""LITReview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.static import serve
from django.conf import settings

from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.views import PasswordResetCompleteView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import PasswordChangeDoneView
from django.shortcuts import redirect

from authentication.views import SignupView
from authentication.views import AccountView

from core.views import CoreViewsHome
from core.views import CoreViewsEmailSent
from core.views import CoreViewsContact

from ticket.views import CreateTicketView
from review.views import CreateReviewView

authpatterns = [
    path('auth/login', LoginView.as_view(
        template_name='authentication/login_page.html',
        redirect_authenticated_user=True
    ), name="login"),
    path('auth/password/reset', PasswordResetView.as_view(
        template_name='authentication/reset_password.html'
    ), name="password_reset"),
    path('auth/password/reset/confirm/<str:uidb64>/<str:token>', PasswordResetConfirmView.as_view(
        template_name='authentication/reset_password_confirm.html',
    ), name="password_reset_confirm"),
    path('auth/password/reset/confirm/done', PasswordResetDoneView.as_view(
        template_name='authentication/reset_password_confirm_done.html'
    ), name="password_reset_done"),
    path('auth/password/reset/confirm/complete', PasswordResetCompleteView.as_view(
        template_name='authentication/reset_password_confirm_complete.html'
    ), name="password_reset_complete"),
    path('auth/password/change', PasswordChangeView.as_view(
        template_name='authentication/change_password.html'
    ), name="password_change"),
    path('auth/password/change/confirm/done', PasswordChangeDoneView.as_view(
        template_name='authentication/change_password_confirm_done.html'
    ), name="password_change_done"),
        
    path('auth/logout', LogoutView.as_view(
        template_name='authentication/logout_page.html',
        redirect_field_name="login"
        ), name="logout"),
    path('auth/signup', SignupView.as_view(), name="signup"),
    path('auth/account', AccountView.as_view(), name="account")
]

ticketpatterns = [
    path('ticket/create', CreateTicketView.as_view(), name="create_ticket")

]

reviewpatterns = [
    path('review/create', CreateReviewView.as_view(), name="create_review")

]

urlpatterns = [
    path('attachments/medias/<path:path>',
     lambda request, path: serve(request, path, document_root=settings.MEDIA_ROOT),
     name="media"),
    path('', lambda request: redirect('home'), name='root'),
    path('admin/', admin.site.urls),
    path('contact/', CoreViewsContact.as_view(), name="contact"),
    path('email-sent/', CoreViewsEmailSent.as_view(), name="email-sent"),
    path('home/', CoreViewsHome.as_view(), name="home")
] + authpatterns + ticketpatterns + reviewpatterns
