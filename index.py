import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# Controllers
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'ico/favicon.ico')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404\

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/imnot/')
def imnot():
    return render_template('imnot.html')

@app.route('/resume/')
def resume():
    return render_template("resume.html")

@app.route('/contact/')
def contact():
    return render_template("contact.html")

@app.route('/photos/')
def photos():
    return render_template("photos.html")
