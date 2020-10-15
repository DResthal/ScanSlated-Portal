from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.views.generic import DetailView, ListView
from .models import Report
from .forms import RegisterForm


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        form.save()
        return redirect(reverse('success'))
    else:
        form = RegisterForm()
    return render(response, 'user_account/register.html', {"form": form})


def success(request):
    return render(request, 'user_account/success.html')


def login(request):
    return render(request, 'user_account/login.html')


def myaccount(request):
    return render(request, 'user_account/myaccount.html')


def reports(request):
    if request.user.is_authenticated:
        reports = request.user.report_set.all()
        return render(request, 'user_account/reports_list.html', {"reports": reports})
    else:
        return redirect(reverse('login'))


def reportdetail(request, id):
    if request.user.is_authenticated:
        report = Report.objects.get(id=id)
        return render(request, 'user_account/report_detail.html', {"report": report})
    else:
        return redirect(reverse('login'))
