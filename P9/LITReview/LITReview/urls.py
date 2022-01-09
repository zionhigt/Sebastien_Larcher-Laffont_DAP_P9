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
from core.views import CoreViewsPost

from ticket.views import CreateTicketView, UpdateTicketView
from ticket.views import ticket_delete_confirm, ticket_delete_by_id
from review.views import CreateReviewView, UpdateReviewView
from review.views import review_delete_confirm, review_delete_by_id

from followers.views import FollowersView

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
    path('ticket/create', CreateTicketView.as_view(), name="create_ticket"),
    path('ticket/update/<int:id>', UpdateTicketView.as_view(), name="update_ticket"),
    path('review/delete/confirm/<int:id>', ticket_delete_confirm, name="delete_ticket_confirm"),
    path('review/delete/<int:id>', ticket_delete_by_id, name="delete_ticket")

]

reviewpatterns = [
    path('review/create/', CreateReviewView.as_view(), name="create_new_review"),
    path('review/create/<int:ticket_id>', CreateReviewView.as_view(), name="create_review"),
    path('review/update/<int:id>', UpdateReviewView.as_view(), name="update_review"),
    path('review/delete/confirm/<int:id>', review_delete_confirm, name="delete_review_confirm"),
    path('review/delete/<int:id>', review_delete_by_id, name="delete_review")

]

urlpatterns = [
    path(
        'core/medias/<path:path>',
        lambda request, path: serve(request, path, document_root=settings.MEDIA_ROOT),
        name="media"
    ),
    path('', lambda request: redirect('home'), name='root'),
    path('admin/', admin.site.urls),
    path('home/', CoreViewsHome.as_view(), name="home"),
    path('post/', CoreViewsPost.as_view(), name="post"),
    path('follow/', FollowersView.as_view(), name="followers_list"),
    path('follow/<int:id>', FollowersView.as_view(), name="following"),
] + authpatterns + ticketpatterns + reviewpatterns
