from flask import Flask, render_template, flash, request, jsonify, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

# DB--------------------------------------------------------------------------------------------




# Invalid URL Handling ---------------------------------------------------------------------------------
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500




# Pages --------------------------------------------------------------------------

@app.route('/')
def home():
    return render_template('index.html')

# Toetse ---------------------------------------------------------------------
@app.route('/flashcard')
def flashcard():
    return render_template('flashcard.html')
@app.route('/multiple')
def multiple():
    return render_template('multiple.html')
@app.route('/invulVrae')
def invulVrae():
    return render_template('invulVrae.html')
@app.route('/skryfToets')
def skryfToets():
    return render_template('skryfToets.html')

# Graad 4 ---------------------------------------------------------------
@app.route('/homegr4')
def homegr4():
    return render_template('homegr4.html')

@app.route('/gr4nw1')
def gr4nw1():
    return render_template('gr4nw1.html')

@app.route('/gr4lv1')
def gr4lv1():
    return render_template('gr4lv1.html')

@app.route('/gr4afr1')
def gr4afr1():
    return render_template('gr4afr1.html')

# Graad 6 ------------------------------------------------
@app.route('/homegr6')
def homegr6():
    return render_template('homegr6.html')

@app.route('/gr6nw1')
def gr6nw1():
    return render_template('gr6nw1.html')

@app.route('/gr6lv1')
def gr6lv1():
    return render_template('gr6lv1.html')

@app.route('/gr6sw1')
def gr6sw1():
    return render_template('gr6sw1.html')
@app.route('/gr6sw1_vrastel')
def gr6sw1_vrastel():
    return render_template('gr6sw1_vrastel.html')

@app.route('/gr4sw1')
def gr4sw1():
    return render_template('gr4sw1.html')



if __name__ == '__main__':
    app.run(debug=True)
