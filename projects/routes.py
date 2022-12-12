from flask import render_template, url_for
from projects import app


@app.route('/')
def home():
    return render_template('portugues.html')


