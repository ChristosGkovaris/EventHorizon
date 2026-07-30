from flask import Flask
from routes.health import health_bp
from routes.docs import docs_bp
from routes.logs import logs_bp


app = Flask(__name__)

app.register_blueprint(health_bp)
app.register_blueprint(docs_bp)
app.register_blueprint(logs_bp)


if __name__ == "__main__":
    app.run(debug=True)