from flask import Flask
from api_routes import api

app = Flask(__name__)
app.register_blueprint(api, url_prefix='/api')

@app.route('/')
def index():
    return "AI-Powered Antivirus Backend is Running!"

if __name__ == '__main__':
    app.run(debug=True)
