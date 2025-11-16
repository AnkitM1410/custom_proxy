from flask import Flask, request, Response
import requests

app = Flask(__name__)

# Groq API base URL
GROQ_API_BASE = "https://api.groq.com"

@app.route('/')
def home():
    return 'Groq API Proxy is running! <br><a href="https://github.com/AnkitM1410">github.com/AnkitM1410</a>'

@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def proxy(path):
    url = f"{GROQ_API_BASE}/{path}"
    params = request.args.to_dict()
    headers = {key: value for key, value in request.headers if key.lower() != 'host'}
    data = request.get_data()
    
    try:
        # Make the request to Groq API
        resp = requests.request(
            method=request.method,
            url=url,
            headers=headers,
            params=params,
            data=data,
            allow_redirects=False
        )
        
        # Create response with Groq's content
        excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        response_headers = [(name, value) for name, value in resp.raw.headers.items()
                           if name.lower() not in excluded_headers]
        
        return Response(resp.content, resp.status_code, response_headers)
    
    except Exception as e:
        return {"error": str(e)}, 500
