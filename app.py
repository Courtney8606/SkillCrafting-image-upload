import os
from flask import Flask, request, render_template

# Create a new Flask app
app = Flask(__name__)

# Configures the app to use the test database if started in test move
if os.getenv('FLASK_ENV') == 'test':
    app.config['TESTING'] = True

# == Your Routes Here ==


# == Example Code Below ==

# This imports some example routes for you to see how they work
# You can delete these lines if you don't need them.
import example_routes

