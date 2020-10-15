from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import redirect
from .forms import RegisterForm

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        form.save()
        return redirect(reverse('user_account/success.html'))
    else:
        form = RegisterForm()
    return render(response, 'user_account/register.html', {"form": form})


def login(request):
    return render(request, 'user_account/login.html')
