from django.contrib import admin
from .models import LoginAttempt

@admin.register(LoginAttempt)
class LoginAttemptAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "ip_address",
        "status",
        "success",
        "created_at",
        "blocked_until",
    )
    list_filter = ("status", "success")
    search_fields = ("username", "ip_address")
