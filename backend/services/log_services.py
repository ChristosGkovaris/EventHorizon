from flask import Blueprint

logs_bp = Blueprint("logs", __name__)


#logs endpoint
@logs_bp.get("/logs") 
def get_logs():
    logs = [
        {
            "id": 1,
            "service": "auth-service",
            "severity": "INFO",
            "message": "User logged in successfully"
        },
        {
            "id": 2,
            "service": "payment-service",
            "severity": "ERROR",
            "message": "Payment request timed out"
        },
        {
            "id": 3,
            "service": "database-service",
            "severity": "WARNING",
            "message": "Database connection pool is almost full"
        }
    ]

    return {
        "logs": logs
    }