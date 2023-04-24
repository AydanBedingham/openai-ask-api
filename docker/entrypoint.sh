#!/bin/sh
gunicorn --log-level=info --chdir /openai-ask-api app:app --workers=2 --threads=2 -b 0.0.0.0:5000
