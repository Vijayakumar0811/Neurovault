from django.db import models
from django.utils import timezone
from datetime import timedelta

class LoginAttempt(models.Model):
    ip_address = models.CharField(max_length=50)
    username = models.CharField(max_length=150)

    success = models.BooleanField(default=False)
    status = models.CharField(max_length=20)  # CLEARED / SUSPICIOUS / BLOCKED

    blocked_until = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def is_currently_blocked(self):
        if self.blocked_until:
            return timezone.now() < self.blocked_until
        return False
from django.db import models

class LogClearMarker(models.Model):
    cleared_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cleared at {self.cleared_at}"
