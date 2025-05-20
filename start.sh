#!/bin/bash

# Fallback to 10000 only if $PORT is not set
PORT=${PORT:-10000}

echo "🛠️ Starting agent on port ${PORT}"

# Start your Flask app using gunicorn
exec gunicorn agent:app --bind 0.0.0.0:$PORT
