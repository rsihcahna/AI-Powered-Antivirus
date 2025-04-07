# /backend/app.py

from flask import Flask
from api_routes import api
from logger import log_event

app = Flask(__name__)
app.register_blueprint(api)

@app.route('/')
def index():
    log_event("Home route accessed")
    return "✅ AI-Powered Antivirus Backend (Flask) is Running!"

if __name__ == '__main__':
    app.run(debug=True)
