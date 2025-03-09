from flask import Flask, render_template, flash, request, jsonify, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

# DB--------------------------------------------------------------------------------------------

# Database Configuration
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Change this to your database URL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Zakkie2910#@localhost/user'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Optional, to suppress warnings
#MySQL db

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mysecret'

# Initialize Database
db = SQLAlchemy(app)
csrf = CSRFProtect(app)

# Database Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<User {self.name}>"

def create_tables():
    with app.app_context():
        db.create_all()

@app.route('/test_db')
def test_db():
    try:
        users = User.query.all()
        return f"Connected! Found {len(users)} users."
    except Exception as e:
        return str(e)



class RegistrationForm(FlaskForm):
    name = StringField('Naam', validators=[DataRequired()])
    email = StringField('Epos', validators=[DataRequired(), Email()])
    submit = SubmitField('Registreer')        

@app.route('/register', methods=['GET', 'POST'])
def register_user():
    form = RegistrationForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data

        if User.query.filter_by(email=email).first():
            flash("Die epos adres is reeds geregistreer!", "warning")
            return redirect(url_for('register_user'))

        new_user = User(name=name, email=email)
        db.session.add(new_user)
        db.session.commit()

        flash("Registrasie suksesvol", "success")
        return redirect(url_for('homegr4'))

    return render_template('register.html', form=form)

@app.route('/user')
def user():
    our_users = User.query.all()  # Fetch all users from the database
    return render_template('user.html', our_users=our_users)






# Invalid URL Handling ---------------------------------------------------------------------------------
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# Create Database
def create_db():
    with app.app_context():
        db.create_all()



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

@app.route('/gr4sw1')
def gr4sw1():
    return render_template('gr4sw1.html')



if __name__ == '__main__':
    app.run(debug=True)
