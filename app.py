from flask import Flask, flash, render_template, request, redirect, url_for, g, session
from functools import wraps
from models.models import *
from scripts.content import *

TUTORIAL_CAT = TutorialCategories()
TOPIC_DICT = Content()

app = Flask(__name__, static_url_path='/static')
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
	return render_template('index.html', title='Home')

@app.route('/contact')
def contact():
	# render the contact page
	return render_template('contact.html', title="Contact")

@app.route('/resume')
def resume():
	# render the resume page
	return render_template('resume.html', title='Resume')

@app.route('/tutorials/<title>/')
@app.route('/tutorials/', defaults= {'title':1})
def tutorials(title):
    if title == 1:
        return render_template("portfolio.html", title='Tutorials', TUTORIAL_CAT = TUTORIAL_CAT)
    else:
        return render_template(title+".html", title=str.title(title), TOPIC_DICT = TOPIC_DICT)

@app.route('/profile')
def profile():
	# render the profile page
	return render_template('profile.html', title='Profile')

@app.route('/blog')
def blog():
	# render the blog page
	return render_template('blog.html', posts=Post.select().order_by(Post.date.desc()), categories=Post.select(Post.category).distinct().order_by(Post.category.asc()))

@app.route('/view')
def view():
	# render the view post page
	return render_template('view.html', title='Viewing Post')

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

@app.route(TOPIC_DICT["Python"][0][1], methods=['GET', 'POST'])
def Hello_World():
    return render_template("tutorials/Python/hello-world.html", curLink = TOPIC_DICT["Python"][0][1], curTitle=TOPIC_DICT["Python"][0][0],  nextLink = TOPIC_DICT["Python"][1][1], nextTitle = TOPIC_DICT["Python"][1][0], curTopic = "Python", title = TOPIC_DICT["Python"][0][0], TOPIC_DICT = TOPIC_DICT)




@app.route(TOPIC_DICT["Python"][1][1], methods=['GET', 'POST'])
def IfElse_Statement():
    return render_template("tutorials/Python/if-else-statement.html", curLink = TOPIC_DICT["Python"][1][1], curTitle=TOPIC_DICT["Python"][1][0],  nextLink = TOPIC_DICT["Python"][2][1], nextTitle = TOPIC_DICT["Python"][2][0], curTopic = "Python", title = TOPIC_DICT["Python"][1][0], TOPIC_DICT = TOPIC_DICT)




@app.route(TOPIC_DICT["Python"][2][1], methods=['GET', 'POST'])
def For_Loop():
    return render_template("tutorials/Python/for-loop.html", curLink = TOPIC_DICT["Python"][2][1], curTitle=TOPIC_DICT["Python"][2][0],  nextLink = TOPIC_DICT["Python"][3][1], nextTitle = TOPIC_DICT["Python"][3][0], curTopic = "Python", title = TOPIC_DICT["Python"][2][0], TOPIC_DICT = TOPIC_DICT)




if __name__ == "__main__":
    app.run(debug=True)
