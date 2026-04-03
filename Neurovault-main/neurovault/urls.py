from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', admin.site.urls),   # 👈 admin opens first
    path('api/', include('security.urls')),
]
