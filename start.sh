#!/bin/bash

echo "⚙️ Starting agent on port ${PORT}"

# Render sets $PORT as an env var, but some shells need it exported
export PORT=${PORT:-10000}  # fallback to 10000 only if unset

# Start the Flask app via gunicorn
exec gunicorn agent:app --bind 0.0.0.0:$PORT
