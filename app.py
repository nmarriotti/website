from flask import Flask, flash, render_template, request, redirect, url_for, g, session, send_from_directory
from functools import wraps
from models.models import *
from scripts.content import *
from werkzeug.utils import secure_filename
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static/uploads')
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'MOV', 'mp4'])

TUTORIAL_CAT = TutorialCategories()
TOPIC_DICT = Content()
BLOG_TOPIC_DICT = BlogContent()

app = Flask(__name__, static_url_path='/static')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
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
        return render_template("portfolio.html", title='Tutorials', TUTORIAL_CAT = TUTORIAL_CAT, count=0, TOPIC_DICT = TOPIC_DICT)
    else:
        return render_template(title+".html", title=str.title(title), TOPIC_DICT = TOPIC_DICT)

@app.route('/profile')
def profile():
	# render the profile page
	return render_template('profile.html', title='Profile')

@app.route('/blog')
def blog():
	# render the blog page
	return render_template('blog.html', posts=Post.select().order_by(Post.date.desc()), categories=Post.select(Post.category).distinct().order_by(Post.category.asc()), title = 'Blog', BLOG_TOPIC_DICT=BLOG_TOPIC_DICT, TUTORIAL_CAT = TUTORIAL_CAT)

@app.route('/view')
def view():
	# render the view post page
	return render_template('view.html', title='Viewing Post')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/dashboard/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part

        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash(filename + ' Uploaded!')
            return render_template('dashboard/upload.html', title='Dashboard', filename = filename)
    return render_template('dashboard/upload.html', title='Dashboard')

@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('dashboard.html', title='Dashboard')

@app.route('/login', methods=['GET', 'POST'])
def do_admin_login():
    if request.method == 'POST':
        if request.form['password'] == 'password' and request.form['username'] == 'admin':
            session['logged_in'] = True
            session['user'] = request.form['username']
            return redirect(url_for('dashboard'))
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





@app.route("/python/"+TOPIC_DICT["Python"][0][1], methods=['GET', 'POST'])
def Hello_World():
    return render_template("tutorials/Python/hello-world.html", curLink = TOPIC_DICT["Python"][0][1], curTitle=TOPIC_DICT["Python"][0][0], curTopic = "Python", title = TOPIC_DICT["Python"][0][0], TOPIC_DICT = TOPIC_DICT, nextTitle= "None")





@app.route("/c++/"+TOPIC_DICT["C++"][0][1], methods=['GET', 'POST'])
def Creating_a_Hello_World_program_in_Cpp():
    return render_template("tutorials/C++/hello-world.html", curLink = TOPIC_DICT["C++"][0][1], curTitle=TOPIC_DICT["C++"][0][0],  nextLink = TOPIC_DICT["C++"][1][1], nextTitle = TOPIC_DICT["C++"][1][0], curTopic = "C++", title = TOPIC_DICT["C++"][0][0], TOPIC_DICT = TOPIC_DICT)

@app.route("/c++/"+TOPIC_DICT["C++"][1][1], methods=['GET', 'POST'])
def Getting_user_input_and_variables():
    return render_template("tutorials/C++/user-input-and-variables.html", curLink = TOPIC_DICT["C++"][1][1], curTitle=TOPIC_DICT["C++"][1][0], curTopic = "C++", title = TOPIC_DICT["C++"][1][0], TOPIC_DICT = TOPIC_DICT, nextTitle= "None")





@app.route("/blog/"+BLOG_TOPIC_DICT["blog"][0][1], methods=['GET', 'POST'])
def Programming_in_Python():
    return render_template("blog/programming-in-python.html", curLink = BLOG_TOPIC_DICT["blog"][0][1], curTitle=BLOG_TOPIC_DICT["blog"][0][0], curTopic = "blog", title = BLOG_TOPIC_DICT["blog"][0][0], BLOG_TOPIC_DICT = BLOG_TOPIC_DICT, TUTORIAL_CAT = TUTORIAL_CAT, nextTitle= "None")

@app.route('/robots.txt')
@app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
