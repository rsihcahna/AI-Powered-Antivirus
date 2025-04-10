# 📄 backend/app.py
# 🚀 Flask Entry Point for AI-Powered Antivirus

from flask import Flask
from api_routes import api

app = Flask(__name__)
app.register_blueprint(api, url_prefix='/api')

@app.route('/')
def index():
    return "🛡️ AI-Powered Antivirus Backend is Running with Flask!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=10000)

