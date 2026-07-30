from flask import Blueprint

docs_bp = Blueprint("docs", __name__)


#docs endpoint
@docs_bp.get("/docs")
def docs():
    return {
        "service": "event-horizon-api",
        "status": "none"
    }