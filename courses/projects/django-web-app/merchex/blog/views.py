from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home_blog(request):
    return render(request, 'blog/home.html')