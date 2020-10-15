from django.urls import path, include
from . import views

app_name = "user_account"
urlpatterns = [
    path(r"register/", views.register, name="register"),
    path('myaccount/', views.myaccount, name="myaccount"),
    path('success/', views.success, name='success'),
    path('reports/', views.reports, name='reports'),
    path('myaccount/report/<int:id>/detail',
         views.reportdetail, name='report_detail'),
]
