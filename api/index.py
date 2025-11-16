from flask import Flask, request, Response
import requests

app = Flask(__name__)
GROQ_API_BASE = "https://api.groq.com"

@app.route('/')
def home():
    return 'Groq API Proxy is running! <br><a href="https://github.com/AnkitM1410">github.com/AnkitM1410</a>'

@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def proxy(path):
    url = f"{GROQ_API_BASE}/{path}"
    params = request.args.to_dict()
    headers = {}
    for key, value in request.headers:
        lower_key = key.lower()
        if lower_key not in ['host', 'accept-encoding']:
            headers[key] = value
    
    # Explicitly request uncompressed response
    headers['Accept-Encoding'] = 'identity'
    data = request.get_data()
    
    try:
        resp = requests.request(
            method=request.method,
            url=url,
            headers=headers,
            params=params,
            data=data,
            allow_redirects=False,
            stream=True
        )
        
        excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection', 'keep-alive']
        response_headers = {}
        
        for name, value in resp.headers.items():
            if name.lower() not in excluded_headers:
                response_headers[name] = value
        
        if 'content-type' not in response_headers:
            response_headers['Content-Type'] = 'application/json'
        
        return Response(
            resp.content, 
            resp.status_code, 
            response_headers
        )
    
    except Exception as e:
        return {"error": str(e)}, 500
