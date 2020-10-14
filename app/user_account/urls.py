from django.urls import path

app_name = 'user_account'
urlpatterns = [
    path(r'', views.home, name='home'),
]
