# security/views.py

from datetime import timedelta
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.utils import timezone
from django.db.models import Count
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import LoginAttempt
from .ip import get_client_ip
from .utils import register_attempt


# ---------------- LOGIN ----------------
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        ip = get_client_ip(request)

        # check block
        last_block = LoginAttempt.objects.filter(
            username=username,
            status="BLOCKED"
        ).order_by("-created_at").first()

        if last_block and last_block.blocked_until:
            if timezone.now() < last_block.blocked_until:
                return render(request, "login.html", {
                    "error": "Account temporarily blocked"
                })

        user = authenticate(request, username=username, password=password)

        if not user:
            register_attempt(ip, username, success=False)
            return render(request, "login.html", {"error": "Invalid credentials"})

        register_attempt(ip, username, success=True)
        login(request, user)
        return render(request, "login.html", {"success": "Login successful"})

    return render(request, "login.html")


# ---------------- DASHBOARD PAGE ----------------
def admin_dashboard_view(request):
    return render(request, "admin_dashboard.html")


# ---------------- LOGS API ----------------
@api_view(["GET"])
def admin_logs_api(request):
    logs = LoginAttempt.objects.order_by("-created_at")[:50]

    return Response({
        "logs": [
            {
                "time": l.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                "ip": l.ip_address,
                "username": l.username,
                "status": l.status
            }
            for l in logs
        ]
    })


# ---------------- DASHBOARD STATS ----------------
@api_view(["GET"])
def dashboard_stats_api(request):
    attempts = LoginAttempt.objects.count()
    threats = LoginAttempt.objects.filter(status="BLOCKED").count()

    confidence = int((threats / attempts) * 100) if attempts else 0

    return Response({
        "attempts": attempts,
        "threats": threats,
        "confidence": confidence
    })


# ---------------- CLEAR LOGS ----------------
@api_view(["POST"])
def clear_logs(request):
    LoginAttempt.objects.all().delete()
    return Response({"message": "Logs cleared"})
