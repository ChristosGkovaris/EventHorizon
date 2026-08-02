from flask import Blueprint, request

logs_bp = Blueprint("logs", __name__)


#logs endpoint
@logs_bp.get("/logs") 
def get_logs():

    # initialization
    requested_severity = request.args.get("severity")
    matching_list = []


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


    # server request
    for i in range(0, len(logs)):
        if requested_severity == logs[i]["severity"]:
            matching_list.append(logs[i])
    return matching_list