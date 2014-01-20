import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return """
           <link href="/static/images/favicon.ico" rel="icon" type="image/x-icon" />
           Hello! Welcome to Adam Goldberg\'s website!
           Coming soon... :)
           """
