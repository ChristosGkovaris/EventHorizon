from flask import Blueprint
from services.log_services import get_logs

logs_bp = Blueprint("logs", __name__)


@logs_bp.get("/logs")
def list_logs():
    logs = get_logs()

    return {
        "logs": logs
    }