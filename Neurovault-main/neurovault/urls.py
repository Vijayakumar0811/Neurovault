from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Neurovault is LIVE 🚀")

urlpatterns = [
    path('', home),   # ✅ ADD THIS LINE
    path('admin/', admin.site.urls),
    path('api/', include('security.urls')),
]
