from django.db import models

class IPAttempt(models.Model):
    ip_address = models.CharField(max_length=50, unique=True)
    attempts = models.IntegerField(default=0)
    last_risk = models.FloatField(default=0.0)
    is_blocked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.ip_address} - {self.attempts} - {'BLOCKED' if self.is_blocked else 'ACTIVE'}"