from flask import Flask
from routes.health import health_bp
from routes.docs import docs_bp
from routes.logs import logs_bp


app = Flask(__name__)

app.register_blueprint(health_bp, url_prefix="/api")
app.register_blueprint(docs_bp, url_prefix="/api")
app.register_blueprint(logs_bp, url_prefix="/api")


if __name__ == "__main__":
    app.run(debug=True)