from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include('api.v1.urls')),
    path('admin/', admin.site.urls),
]