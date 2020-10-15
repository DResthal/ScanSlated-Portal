from django.urls import path
from . import views

app_name = 'website'
urlpatterns = [
    path(r'', views.home, name='home'),
]
