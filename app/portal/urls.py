from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('website.urls')),
    path('user_account/', include('user_account.urls')),
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
]
