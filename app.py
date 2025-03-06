from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

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

@app.route('/gr4swg1')
def gr4swg1():
    return render_template('gr4swg1.html')

@app.route('/header')
def header():
    return render_template('header.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

#Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

#Internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500













if __name__ == '__main__':
    app.run(debug=True)
