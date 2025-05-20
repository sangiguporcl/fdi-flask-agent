#!/bin/bash

# Use Render's dynamic PORT without fallback
echo "🟢 Starting agent on port: ${PORT}"

# Start app with gunicorn on the provided port
exec gunicorn agent:app --bind 0.0.0.0:${PORT}
