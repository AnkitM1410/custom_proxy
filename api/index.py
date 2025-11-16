from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def proxy_all_requests(path):
    target_url = f"https://api.groq.com/{path}"
    headers = dict(request.headers)
    headers.pop('Host', None)
    
    try:
        if request.method == 'GET':
            resp = requests.get(target_url, headers=headers, timeout=30)
        elif request.method == 'POST':
            resp = requests.post(target_url, headers=headers, data=request.get_data(), timeout=30)
        elif request.method == 'PUT':
            resp = requests.put(target_url, headers=headers, data=request.get_data(), timeout=30)
        elif request.method == 'DELETE':
            resp = requests.delete(target_url, headers=headers, timeout=30)
        
        # Return the response from Groq
        return jsonify(resp.json()), resp.status_code
        
    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run()