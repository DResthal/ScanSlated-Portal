from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.views.generic import DetailView, ListView
from .models import Report
from .forms import RegisterForm

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        form.save()
        return redirect('user_account/success')
    else:
        form = RegisterForm()
    return render(response, 'user_account/register.html', {"form": form})

def success(request):
    return render(request, 'user_account/success.html')

def login(request):
    return render(request, 'user_account/login.html')

def myaccount(request):
    return render(request, 'user_account/myaccount.html')

class Reports(ListView):
    model = Report
    context_object_name = 'reports'
    template_name ='user_account/reports_list.html'

    def get_query_set(self):
        return request.User.reports_set.all()

class ReportDetail(DetailView):
    model = Report
    context_object_name = 'report'
    template_name = 'user_account/report_detail.html'