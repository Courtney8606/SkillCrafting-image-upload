#!/bin/sh

echo "Run this script to start the web server for testing"
echo "Once you have started it, run 'pipenv run pytest' in another terminal."
echo "Starting..."
FLASK_ENV=test pipenv run flask --debug run
