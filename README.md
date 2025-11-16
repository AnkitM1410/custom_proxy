# Custom Proxy

A simple Flask-based proxy server that forwards requests to the Groq API.

## What it does

This proxy server acts as an intermediary between your applications and the Groq API. It forwards all HTTP requests (GET, POST, PUT, DELETE, PATCH) to the Groq API while preserving headers, query parameters, and request bodies.

## Running Locally

```bash
python api/index.py
```

Your proxy server will be available at `http://localhost:5000` or `https://groqproxy.vercel.app`.

## Usage

Send requests to your proxy server instead of directly to the Groq API. The proxy will forward them automatically.
