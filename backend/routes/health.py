from flask import Blueprint

health_bp = Blueprint("health", __name__)


#health endpoint
@health_bp.get("/api/health") 
def health():
    return {
        "service": "event-horizon-api",
        "status": "healthy"
    }