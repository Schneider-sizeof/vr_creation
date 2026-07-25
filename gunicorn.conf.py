"""
Gunicorn configuration for VR Creation Company.
Usage: gunicorn config.wsgi:application -c gunicorn.conf.py
"""
import multiprocessing
import os

# Server socket
bind = os.environ.get('GUNICORN_BIND', '0.0.0.0:8000')

# Worker processes
workers = int(os.environ.get('GUNICORN_WORKERS', multiprocessing.cpu_count() * 2 + 1))
worker_class = 'sync'
worker_connections = 1000
timeout = 120
keepalive = 5

# Logging
accesslog = '-'
errorlog = '-'
loglevel = os.environ.get('GUNICORN_LOG_LEVEL', 'info')

# Process naming
proc_name = 'vrcreation'

# Security
limit_request_line = 4094
limit_request_fields = 100
limit_request_field_size = 8190
