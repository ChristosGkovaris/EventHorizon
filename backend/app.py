from flask import Flask

app = Flask(__name__)


@app.get("/api/health")
def health():
    return {
        "service": "event-horizon-api",
        "status": "healthy"
    }

@app.get("/api/me")
def test():
    return {
        "message": "hello !"
    }

if __name__ == "__main__":
    app.run(debug=True)