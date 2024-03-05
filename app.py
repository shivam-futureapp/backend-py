from flask import Flask, jsonify
from flask_cors import CORS

backend_app = Flask(__name__)
CORS(backend_app)  # Enable CORS for all routes in the backend app

@backend_app.route('/api/hello')
def hello():
    return jsonify({'message': 'Hello from the backend! everything works fine'})

if __name__ == '__main__':
    backend_app.run(host='0.0.0.0', port=83)  # Run the backend app on port 5001
