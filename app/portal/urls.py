from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(r'', include('website.urls')),
    path(r'user_account/', include('user_account.urls')),
    path('admin/', admin.site.urls),
    path(r'', include('django.contrib.auth.urls')),
]
