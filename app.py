from flask import Flask, flash, render_template, request, redirect, url_for, g, session
from functools import wraps
from models.models import *

app = Flask(__name__)
app.secret_key = 'some_secret'



@app.before_request
def before_request():
	# create db if needed and connect
	initialize_db()



@app.teardown_request
def teardown_request(exception):
	# close the db connection
	db.close()



@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404



@app.route('/')
def home():
	# render the home page
	return render_template('index.html')



@app.route('/contact')
def contact():
	# render the contact page
	return render_template('contact.html')



@app.route('/resume')
def resume():
	# render the resume page
	return render_template('resume.html')



@app.route('/portfolio')
def portfolio():
	# render the portfolio page
	return render_template('portfolio.html')


@app.route('/profile')
def profile():
	# render the profile page
	return render_template('profile.html')



@app.route('/blog')
def blog():
	# render the blog page
	return render_template('blog.html', posts=Post.select().order_by(Post.date.desc()), categories=Post.select(Post.category).distinct().order_by(Post.category.asc()))



@app.route('/view')
def view():
	# render the view post page
	return render_template('view.html')



@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('dashboard.html')



@app.route('/login', methods=['GET', 'POST'])
def do_admin_login():
    if request.method == 'POST':
        if request.form['password'] == 'password' and request.form['username'] == 'admin':
            session['logged_in'] = True
            session['user'] = request.form['username']
            return render_template('dashboard.html')
        else:
            flash('Invalid username and/or password!')
            return render_template('login.html')
    else:
        return render_template('login.html')



@app.route('/register', methods=['GET', 'POST'])
def register():
	# render the view register page
	return render_template('create_account.html')



@app.route("/logout")
def logout():
    session['logged_in'] = False
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
