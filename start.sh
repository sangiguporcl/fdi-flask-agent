#!/usr/bin/env bash
echo "⚙️ Starting agent on port $PORT"
exec gunicorn agent:app --bind 0.0.0.0:$PORT
