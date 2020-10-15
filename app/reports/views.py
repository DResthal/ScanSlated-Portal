from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.views.generic import DetailView, ListView
from .models import Report, ReportField

# Get All


class GetAllReports(ListView):
    model = Report
    context_object_name = "report"
    return(Report.objects.all())

# Get One

# Create

# Update

# Delete
