from rest_framework.decorators import api_view
from rest_framework.response import Response
from .ai_engine import predict
from .models import IPAttempt

RISK_THRESHOLD = 0.6
MAX_ATTEMPTS = 5

@api_view(["POST"])
def analyze_login(request):
    data = request.data

    try:
        ip_address = data.get("ip_address")

        features = [
            float(data.get("ip_num", 0)),
            float(data.get("login_time_sec", 0)),
            float(data.get("round_trip_time_ms", 0)),
            float(data.get("country", 0)),
            float(data.get("region", 0)),
            float(data.get("city", 0)),
            float(data.get("browser", 0)),
            float(data.get("os", 0)),
            float(data.get("device", 0)),
            float(data.get("login_successful", 0)),
            float(data.get("asn", 0)),
        ]

        # Run AI
        result = predict(features)

        ip_obj, created = IPAttempt.objects.get_or_create(ip_address=ip_address)

        # If already blocked
        if ip_obj.is_blocked:
            return Response({
                "blocked": True,
                "attempts": ip_obj.attempts,
                "message": "This IP is blocked"
            })

        # Increase attempts if risky
        if result["risk_score"] > RISK_THRESHOLD or data.get("login_successful") == 0:
            ip_obj.attempts += 1
            ip_obj.last_risk = result["risk_score"]

            if ip_obj.attempts >= MAX_ATTEMPTS:
                ip_obj.is_blocked = True

            ip_obj.save()

        return Response({
            "risk_score": result["risk_score"],
            "is_attack": result["is_attack"],
            "attempts": ip_obj.attempts,
            "blocked": ip_obj.is_blocked,
            "confidence": result["confidence"]
        })

    except Exception as e:
        return Response({"error": str(e)}, status=400)