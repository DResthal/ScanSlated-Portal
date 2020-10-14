from django.shortcuts import render

def home(request):
    return render(request, 'user_account/home')
