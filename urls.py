from django.urls import path
from .views import (
    login_view,
    admin_dashboard_view,
    admin_logs_api,
    dashboard_stats_api,
    clear_logs
)

urlpatterns = [
    path("", login_view),
    path("nv-vault/", admin_dashboard_view),
    path("admin-logs/", admin_logs_api),
    path("dashboard-stats/", dashboard_stats_api),
    path("clear-logs/", clear_logs),
]

