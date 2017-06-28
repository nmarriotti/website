from flask import Flask, flash, render_template, request, redirect, url_for, g, session, send_from_directory
from functools import wraps
from models.models import *
from scripts.content import *
from whitenoise import WhiteNoise
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


@app.route('/tutorials/<title>/')
@app.route('/tutorials/', defaults= {'title':1})
def tutorials(title):
    if title == 1:
        return render_template("portfolio.html", title='Tutorials', TUTORIAL_CAT = TUTORIAL_CAT, count=0, TOPIC_DICT = TOPIC_DICT)
    else:
        return render_template(title+".html", title=str.title(title), TOPIC_DICT = TOPIC_DICT)


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


@app.route("/tutorials/python/"+TOPIC_DICT["Python"][0][1], methods=['GET', 'POST'])
def Getting_Started_with_Python():
    return render_template("tutorials/Python/getting-started-with-python.html", curLink = TOPIC_DICT["Python"][0][1], curTitle=TOPIC_DICT["Python"][0][0],  nextLink = TOPIC_DICT["Python"][1][1], nextTitle = TOPIC_DICT["Python"][1][0], curTopic = "Python", title = TOPIC_DICT["Python"][0][0], TOPIC_DICT = TOPIC_DICT)

@app.route("/tutorials/python/"+TOPIC_DICT["Python"][1][1], methods=['GET', 'POST'])
def Creating_a_Hello_World_program_in_Python():
    return render_template("tutorials/Python/hello-world.html", curLink = TOPIC_DICT["Python"][1][1], curTitle=TOPIC_DICT["Python"][1][0], curTopic = "Python", title = TOPIC_DICT["Python"][1][0], TOPIC_DICT = TOPIC_DICT, nextTitle=TOPIC_DICT["Python"][2][0], nextLink=TOPIC_DICT["Python"][2][1])
	

@app.route("/tutorials/python/"+TOPIC_DICT["Python"][2][1], methods=['GET', 'POST'])
def How_to_use_variables():
    return render_template("tutorials/Python/how-to-use-variables.html", curLink = TOPIC_DICT["Python"][2][1], curTitle=TOPIC_DICT["Python"][2][0], curTopic = "Python", title = TOPIC_DICT["Python"][2][0], TOPIC_DICT = TOPIC_DICT, nextTitle=TOPIC_DICT["Python"][3][0], nextLink=TOPIC_DICT["Python"][3][1])


@app.route("/tutorials/python/"+TOPIC_DICT["Python"][3][1], methods=['GET', 'POST'])
def Functions():
    return render_template("tutorials/Python/functions.html", curLink = TOPIC_DICT["Python"][3][1], curTitle=TOPIC_DICT["Python"][3][0], curTopic = "Python", title = TOPIC_DICT["Python"][3][0], TOPIC_DICT = TOPIC_DICT, nextTitle= TOPIC_DICT["Python"][4][0], nextLink=TOPIC_DICT["Python"][4][1])


@app.route("/tutorials/python/"+TOPIC_DICT["Python"][4][1], methods=['GET', 'POST'])
def Using_lists_to_store_information():
    return render_template("tutorials/Python/using-lists-to-store-information.html", curLink = TOPIC_DICT["Python"][4][1], curTitle=TOPIC_DICT["Python"][4][0], curTopic = "Python", title = TOPIC_DICT["Python"][4][0], TOPIC_DICT = TOPIC_DICT, nextTitle= TOPIC_DICT["Python"][5][0], nextLink=TOPIC_DICT["Python"][5][1])


@app.route("/tutorials/python/"+TOPIC_DICT["Python"][5][1], methods=['GET', 'POST'])
def Storing_information_in_dictionaries():
    return render_template("tutorials/Python/storing-information-in-dictionaries.html", curLink = TOPIC_DICT["Python"][5][1], curTitle=TOPIC_DICT["Python"][5][0], curTopic = "Python", title = TOPIC_DICT["Python"][5][0], TOPIC_DICT = TOPIC_DICT, nextTitle= TOPIC_DICT["Python"][6][0], nextLink=TOPIC_DICT["Python"][6][1])


@app.route("/tutorials/python/"+TOPIC_DICT["Python"][6][1], methods=['GET', 'POST'])
def Lambda_Functions():
    return render_template("tutorials/Python/lambda-functions.html", curLink = TOPIC_DICT["Python"][6][1], curTitle=TOPIC_DICT["Python"][6][0], curTopic = "Python", title = TOPIC_DICT["Python"][6][0], TOPIC_DICT = TOPIC_DICT, nextTitle=TOPIC_DICT["Python"][7][0], nextLink=TOPIC_DICT["Python"][7][1])


@app.route("/tutorials/python/"+TOPIC_DICT["Python"][7][1], methods=['GET', 'POST'])
def If_Statements():
    return render_template("tutorials/Python/if-statements.html", curLink = TOPIC_DICT["Python"][7][1], curTitle=TOPIC_DICT["Python"][7][0], curTopic = "Python", title = TOPIC_DICT["Python"][7][0], TOPIC_DICT = TOPIC_DICT, nextTitle=TOPIC_DICT["Python"][8][0], nextLink=TOPIC_DICT["Python"][8][1])


@app.route("/tutorials/python/"+TOPIC_DICT["Python"][8][1], methods=['GET', 'POST'])
def python_Loops():
    return render_template("tutorials/Python/loops.html", curLink = TOPIC_DICT["Python"][8][1], curTitle=TOPIC_DICT["Python"][8][0], curTopic = "Python", title = TOPIC_DICT["Python"][8][0], TOPIC_DICT = TOPIC_DICT, nextTitle=TOPIC_DICT["Python"][9][0], nextLink=TOPIC_DICT["Python"][9][1])


@app.route("/tutorials/python/"+TOPIC_DICT["Python"][9][1], methods=['GET', 'POST'])
def Error_Handling():
    return render_template("tutorials/Python/error-handling.html", curLink = TOPIC_DICT["Python"][9][1], curTitle=TOPIC_DICT["Python"][9][0], curTopic = "Python", title = TOPIC_DICT["Python"][9][0], TOPIC_DICT = TOPIC_DICT, nextTitle=TOPIC_DICT["Python"][10][0], nextLink=TOPIC_DICT["Python"][10][1])


@app.route("/tutorials/python/"+TOPIC_DICT["Python"][10][1], methods=['GET', 'POST'])
def Writing_to_a_File():
    return render_template("tutorials/Python/writing-to-a-file.html", curLink = TOPIC_DICT["Python"][10][1], curTitle=TOPIC_DICT["Python"][10][0], curTopic = "Python", title = TOPIC_DICT["Python"][10][0], TOPIC_DICT = TOPIC_DICT, nextTitle=TOPIC_DICT["Python"][11][0], nextLink=TOPIC_DICT["Python"][11][1])


@app.route("/tutorials/python/"+TOPIC_DICT["Python"][11][1], methods=['GET', 'POST'])
def Reading_from_a_File():
    return render_template("tutorials/Python/reading-from-a-file.html", curLink = TOPIC_DICT["Python"][11][1], curTitle=TOPIC_DICT["Python"][11][0], curTopic = "Python", title = TOPIC_DICT["Python"][11][0], TOPIC_DICT = TOPIC_DICT, nextTitle=TOPIC_DICT["Python"][12][0], nextLink=TOPIC_DICT["Python"][12][1])


@app.route("/tutorials/python/"+TOPIC_DICT["Python"][12][1], methods=['GET', 'POST'])
def DOCSTRING():
    return render_template("tutorials/Python/docstring.html", curLink = TOPIC_DICT["Python"][12][1], curTitle=TOPIC_DICT["Python"][12][0], curTopic = "Python", title = TOPIC_DICT["Python"][12][0], TOPIC_DICT = TOPIC_DICT, nextTitle=TOPIC_DICT["Python"][13][0], nextLink=TOPIC_DICT["Python"][13][1])


@app.route("/tutorials/python/"+TOPIC_DICT["Python"][13][1], methods=['GET', 'POST'])
def Python_Classes_and_Objects():
    return render_template("tutorials/Python/classes-and-objects.html", curLink = TOPIC_DICT["Python"][13][1], curTitle=TOPIC_DICT["Python"][13][0], curTopic = "Python", title = TOPIC_DICT["Python"][13][0], TOPIC_DICT = TOPIC_DICT, nextTitle=TOPIC_DICT["Python"][14][0], nextLink=TOPIC_DICT["Python"][14][1])


@app.route("/tutorials/python/"+TOPIC_DICT["Python"][14][1], methods=['GET', 'POST'])
def Class_Inheritance():
    return render_template("tutorials/Python/class-inheritance.html", curLink = TOPIC_DICT["Python"][14][1], curTitle=TOPIC_DICT["Python"][14][0], curTopic = "Python", title = TOPIC_DICT["Python"][14][0], TOPIC_DICT = TOPIC_DICT, nextTitle=TOPIC_DICT["Python"][15][0], nextLink=TOPIC_DICT["Python"][15][1])


@app.route("/tutorials/python/"+TOPIC_DICT["Python"][15][1], methods=['GET', 'POST'])
def Queue_Tutorial():
    return render_template("tutorials/Python/queues.html", curLink = TOPIC_DICT["Python"][15][1], curTitle=TOPIC_DICT["Python"][15][0], curTopic = "Python", title = TOPIC_DICT["Python"][15][0], TOPIC_DICT = TOPIC_DICT, nextTitle=TOPIC_DICT["Python"][16][0], nextLink=TOPIC_DICT["Python"][16][1])


@app.route("/tutorials/python/"+TOPIC_DICT["Python"][16][1], methods=['GET', 'POST'])
def Processing_Queue_with_Multi_threading():
    return render_template("tutorials/Python/processing-queue-with-multi-threading.html", curLink = TOPIC_DICT["Python"][16][1], curTitle=TOPIC_DICT["Python"][16][0], curTopic = "Python", title = TOPIC_DICT["Python"][16][0], TOPIC_DICT = TOPIC_DICT, nextTitle=TOPIC_DICT["Python"][17][0], nextLink=TOPIC_DICT["Python"][17][1])


@app.route("/tutorials/python/"+TOPIC_DICT["Python"][17][1], methods=['GET', 'POST'])
def Zip_Files():
    return render_template("tutorials/Python/zip-files.html", curLink = TOPIC_DICT["Python"][17][1], curTitle=TOPIC_DICT["Python"][17][0], curTopic = "Python", title = TOPIC_DICT["Python"][17][0], TOPIC_DICT = TOPIC_DICT, nextTitle=TOPIC_DICT["Python"][18][0], nextLink=TOPIC_DICT["Python"][18][1])

@app.route("/tutorials/python/"+TOPIC_DICT["Python"][18][1], methods=['GET', 'POST'])
def Command_Line_Arguments_using_argparse():
    return render_template("tutorials/Python/command-line-arguments-using-argparse.html", curLink = TOPIC_DICT["Python"][18][1], curTitle=TOPIC_DICT["Python"][18][0], curTopic = "Python", title = TOPIC_DICT["Python"][18][0], TOPIC_DICT = TOPIC_DICT, nextTitle= "None")


@app.route("/tutorials/c/"+TOPIC_DICT["C"][0][1], methods=['GET', 'POST'])
def Hello_World_in_C():
    return render_template("tutorials/C/hello-world.html", curLink = TOPIC_DICT["C"][0][1], curTitle=TOPIC_DICT["C"][0][0], curTopic = "C", title = TOPIC_DICT["C"][0][0], TOPIC_DICT = TOPIC_DICT, nextTitle= TOPIC_DICT["C"][1][0], nextLink=TOPIC_DICT["C"][1][1])


@app.route("/tutorials/c/"+TOPIC_DICT["C"][1][1], methods=['GET', 'POST'])
def Printing_variables_with_printf():
    return render_template("tutorials/C/printing-variables-with-printf.html", curLink = TOPIC_DICT["C"][1][1], curTitle=TOPIC_DICT["C"][1][0], curTopic = "C", title = TOPIC_DICT["C"][1][0], TOPIC_DICT = TOPIC_DICT, nextTitle=TOPIC_DICT["C"][2][0], nextLink=TOPIC_DICT["C"][2][1])


@app.route("/tutorials/c/"+TOPIC_DICT["C"][2][1], methods=['GET', 'POST'])
def Command_Line_Arguments():
    return render_template("tutorials/C/command-line-arguments.html", curLink = TOPIC_DICT["C"][2][1], curTitle=TOPIC_DICT["C"][2][0], curTopic = "C", title = TOPIC_DICT["C"][2][0], TOPIC_DICT = TOPIC_DICT, nextTitle= TOPIC_DICT["C"][3][0], nextLink=TOPIC_DICT["C"][3][1])


@app.route("/tutorials/c/"+TOPIC_DICT["C"][3][1], methods=['GET', 'POST'])
def User_Input():
    return render_template("tutorials/C/user-input.html", curLink = TOPIC_DICT["C"][3][1], curTitle=TOPIC_DICT["C"][3][0], curTopic = "C", title = TOPIC_DICT["C"][3][0], TOPIC_DICT = TOPIC_DICT, nextTitle= TOPIC_DICT["C"][4][0], nextLink=TOPIC_DICT["C"][4][1])


@app.route("/tutorials/c/"+TOPIC_DICT["C"][4][1], methods=['GET', 'POST'])
def Creating_Header_Files():
    return render_template("tutorials/C/creating-header-files.html", curLink = TOPIC_DICT["C"][4][1], curTitle=TOPIC_DICT["C"][4][0], curTopic = "C", title = TOPIC_DICT["C"][4][0], TOPIC_DICT = TOPIC_DICT, nextTitle=TOPIC_DICT["C"][5][0], nextLink=TOPIC_DICT["C"][5][1])


@app.route("/tutorials/c/"+TOPIC_DICT["C"][5][1], methods=['GET', 'POST'])
def Using_Structs():
    return render_template("tutorials/C/structs.html", curLink = TOPIC_DICT["C"][5][1], curTitle=TOPIC_DICT["C"][5][0], curTopic = "C", title = TOPIC_DICT["C"][5][0], TOPIC_DICT = TOPIC_DICT, nextTitle=TOPIC_DICT["C"][6][0], nextLink=TOPIC_DICT["C"][6][1])


@app.route("/tutorials/c/"+TOPIC_DICT["C"][6][1], methods=['GET', 'POST'])
def Using_Union():
    return render_template("tutorials/C/union.html", curLink = TOPIC_DICT["C"][6][1], curTitle=TOPIC_DICT["C"][6][0], curTopic = "C", title = TOPIC_DICT["C"][6][0], TOPIC_DICT = TOPIC_DICT, nextTitle=TOPIC_DICT["C"][7][0], nextLink=TOPIC_DICT["C"][7][1])


@app.route("/tutorials/c/"+TOPIC_DICT["C"][7][1], methods=['GET', 'POST'])
def Switch_Statement():
    return render_template("tutorials/C/switch-statement.html", curLink = TOPIC_DICT["C"][7][1], curTitle=TOPIC_DICT["C"][7][0], curTopic = "C", title = TOPIC_DICT["C"][7][0], TOPIC_DICT = TOPIC_DICT, nextTitle=TOPIC_DICT["C"][8][0], nextLink=TOPIC_DICT["C"][8][1])


@app.route("/tutorials/c/"+TOPIC_DICT["C"][8][1], methods=['GET', 'POST'])
def Writing_Files_C():
    return render_template("tutorials/C/writing-files.html", curLink = TOPIC_DICT["C"][8][1], curTitle=TOPIC_DICT["C"][8][0], curTopic = "C", title = TOPIC_DICT["C"][8][0], TOPIC_DICT = TOPIC_DICT, nextTitle= TOPIC_DICT["C"][9][0], nextLink=TOPIC_DICT["C"][9][1])


@app.route("/tutorials/c/"+TOPIC_DICT["C"][9][1], methods=['GET', 'POST'])
def C_Reading_Files():
    return render_template("tutorials/C/reading-files.html", curLink = TOPIC_DICT["C"][9][1], curTitle=TOPIC_DICT["C"][9][0], curTopic = "C", title = TOPIC_DICT["C"][9][0], TOPIC_DICT = TOPIC_DICT, nextTitle= TOPIC_DICT["C"][10][0], nextLink=TOPIC_DICT["C"][10][1])


@app.route("/tutorials/c/"+TOPIC_DICT["C"][10][1], methods=['GET', 'POST'])
def C_Functions():
    return render_template("tutorials/C/functions.html", curLink = TOPIC_DICT["C"][10][1], curTitle=TOPIC_DICT["C"][10][0], curTopic = "C", title = TOPIC_DICT["C"][10][0], TOPIC_DICT = TOPIC_DICT, nextTitle= TOPIC_DICT["C"][11][0], nextLink=TOPIC_DICT["C"][11][1])


@app.route("/tutorials/c/"+TOPIC_DICT["C"][11][1], methods=['GET', 'POST'])
def Pointers():
    return render_template("tutorials/C/pointers.html", curLink = TOPIC_DICT["C"][11][1], curTitle=TOPIC_DICT["C"][11][0], curTopic = "C", title = TOPIC_DICT["C"][11][0], TOPIC_DICT = TOPIC_DICT, nextTitle= TOPIC_DICT["C"][12][0], nextLink=TOPIC_DICT["C"][12][1])

@app.route("/tutorials/c/"+TOPIC_DICT["C"][12][1], methods=['GET', 'POST'])
def Split_strings_using_strtok():
    return render_template("tutorials/C/split-strings-using-strtok.html", curLink = TOPIC_DICT["C"][12][1], curTitle=TOPIC_DICT["C"][12][0], curTopic = "C", title = TOPIC_DICT["C"][12][0], TOPIC_DICT = TOPIC_DICT, nextTitle=TOPIC_DICT["C"][13][0], nextLink=TOPIC_DICT["C"][13][1])


@app.route("/tutorials/c/"+TOPIC_DICT["C"][13][1], methods=['GET', 'POST'])
def Parsing_CSV_File():
    return render_template("tutorials/C/parsing-csv-file.html", curLink = TOPIC_DICT["C"][13][1], curTitle=TOPIC_DICT["C"][13][0], curTopic = "C", title = TOPIC_DICT["C"][13][0], TOPIC_DICT = TOPIC_DICT, nextTitle= "None")



@app.route("/tutorials/c++/"+TOPIC_DICT["C++"][0][1], methods=['GET', 'POST'])
def Installing_the_Cpp_compiler_and_CodeBlocks_IDE():
    return render_template("tutorials/C++/installing-compiler-and-codeblocks-ide.html", curLink = TOPIC_DICT["C++"][0][1], curTitle=TOPIC_DICT["C++"][0][0],  nextLink = TOPIC_DICT["C++"][1][1], nextTitle = TOPIC_DICT["C++"][1][0], curTopic = "C++", title = TOPIC_DICT["C++"][0][0], TOPIC_DICT = TOPIC_DICT)




@app.route("/tutorials/c++/"+TOPIC_DICT["C++"][1][1], methods=['GET', 'POST'])
def Creating_a_Hello_World_program_in_Cpp():
    return render_template("tutorials/C++/hello-world.html", curLink = TOPIC_DICT["C++"][1][1], curTitle=TOPIC_DICT["C++"][1][0], curTopic = "C++", title = TOPIC_DICT["C++"][1][0], TOPIC_DICT = TOPIC_DICT, nextLink = TOPIC_DICT["C++"][2][1], nextTitle= TOPIC_DICT["C++"][2][0])

@app.route("/tutorials/c++/"+TOPIC_DICT["C++"][2][1], methods=['GET', 'POST'])
def Getting_user_input_and_variables():
    return render_template("tutorials/C++/user-input-and-variables.html", curLink = TOPIC_DICT["C++"][2][1], curTitle=TOPIC_DICT["C++"][2][0], curTopic = "C++", title = TOPIC_DICT["C++"][2][0], TOPIC_DICT = TOPIC_DICT, nextLink = TOPIC_DICT["C++"][3][1], nextTitle= TOPIC_DICT["C++"][3][0])

@app.route("/tutorials/c++/"+TOPIC_DICT["C++"][3][1], methods=['GET', 'POST'])
def Data_Types():
    return render_template("tutorials/C++/data-types.html", curLink = TOPIC_DICT["C++"][3][1], curTitle=TOPIC_DICT["C++"][3][0], curTopic = "C++", title = TOPIC_DICT["C++"][3][0], TOPIC_DICT = TOPIC_DICT, nextLink = TOPIC_DICT["C++"][4][1], nextTitle= TOPIC_DICT["C++"][4][0])

@app.route("/tutorials/c++/"+TOPIC_DICT["C++"][4][1], methods=['GET', 'POST'])
def Conditional_Statements():
    return render_template("tutorials/C++/conditional-statements.html", curLink = TOPIC_DICT["C++"][4][1], curTitle=TOPIC_DICT["C++"][4][0], curTopic = "C++", title = TOPIC_DICT["C++"][4][0], TOPIC_DICT = TOPIC_DICT, nextLink = TOPIC_DICT["C++"][5][1], nextTitle = TOPIC_DICT["C++"][5][0])

@app.route("/tutorials/c++/"+TOPIC_DICT["C++"][5][1], methods=['GET', 'POST'])
def Loops():
    return render_template("tutorials/C++/loops.html", curLink = TOPIC_DICT["C++"][5][1], curTitle=TOPIC_DICT["C++"][5][0], curTopic = "C++", title = TOPIC_DICT["C++"][5][0], TOPIC_DICT = TOPIC_DICT, nextLink=TOPIC_DICT["C++"][6][1], nextTitle= TOPIC_DICT["C++"][6][0])
	

@app.route("/tutorials/c++/"+TOPIC_DICT["C++"][6][1], methods=['GET', 'POST'])
def How_to_create_and_use_functions():
    return render_template("tutorials/C++/how-to-create-and-use-functions.html", curLink = TOPIC_DICT["C++"][6][1], curTitle=TOPIC_DICT["C++"][6][0], curTopic = "C++", title = TOPIC_DICT["C++"][6][0], TOPIC_DICT = TOPIC_DICT, nextLink = TOPIC_DICT["C++"][7][1], nextTitle = TOPIC_DICT["C++"][7][0])


@app.route("/tutorials/c++/"+TOPIC_DICT["C++"][7][1], methods=['GET', 'POST'])
def Arrays():
    return render_template("tutorials/C++/arrays.html", curLink = TOPIC_DICT["C++"][7][1], curTitle=TOPIC_DICT["C++"][7][0], curTopic = "C++", title = TOPIC_DICT["C++"][7][0], TOPIC_DICT = TOPIC_DICT, nextTitle= TOPIC_DICT["C++"][8][0], nextLink = TOPIC_DICT["C++"][8][1])	


@app.route("/tutorials/c++/"+TOPIC_DICT["C++"][8][1], methods=['GET', 'POST'])
def Writing_Files():
    return render_template("tutorials/C++/writing-files.html", curLink = TOPIC_DICT["C++"][8][1], curTitle=TOPIC_DICT["C++"][8][0], curTopic = "C++", title = TOPIC_DICT["C++"][8][0], TOPIC_DICT = TOPIC_DICT, nextTitle= TOPIC_DICT["C++"][9][0], nextLink=TOPIC_DICT["C++"][9][1])


@app.route("/tutorials/c++/"+TOPIC_DICT["C++"][9][1], methods=['GET', 'POST'])
def Reading_Files():
    return render_template("tutorials/C++/reading-files.html", curLink = TOPIC_DICT["C++"][9][1], curTitle=TOPIC_DICT["C++"][9][0], curTopic = "C++", title = TOPIC_DICT["C++"][9][0], TOPIC_DICT = TOPIC_DICT, nextTitle= TOPIC_DICT["C++"][10][0], nextLink=TOPIC_DICT["C++"][10][1])


@app.route("/tutorials/c++/"+TOPIC_DICT["C++"][10][1], methods=['GET', 'POST'])
def Reading_CSV_Files():
    return render_template("tutorials/C++/reading-csv-files.html", curLink = TOPIC_DICT["C++"][10][1], curTitle=TOPIC_DICT["C++"][10][0], curTopic = "C++", title = TOPIC_DICT["C++"][10][0], TOPIC_DICT = TOPIC_DICT, nextTitle= TOPIC_DICT["C++"][11][0], nextLink=TOPIC_DICT["C++"][11][1])
	

@app.route("/tutorials/c++/"+TOPIC_DICT["C++"][11][1], methods=['GET', 'POST'])
def Classes_and_Objects():
    return render_template("tutorials/C++/classes-and-objects.html", curLink = TOPIC_DICT["C++"][11][1], curTitle=TOPIC_DICT["C++"][11][0], curTopic = "C++", title = TOPIC_DICT["C++"][11][0], TOPIC_DICT = TOPIC_DICT, nextTitle=TOPIC_DICT["C++"][12][0], nextLink=TOPIC_DICT["C++"][12][1])


	
@app.route("/tutorials/c++/"+TOPIC_DICT["C++"][12][1], methods=['GET', 'POST'])
def Pointers_and_References():
    return render_template("tutorials/C++/pointers-and-references.html", curLink = TOPIC_DICT["C++"][12][1], curTitle=TOPIC_DICT["C++"][12][0], curTopic = "C++", title = TOPIC_DICT["C++"][12][0], TOPIC_DICT = TOPIC_DICT, nextTitle= "None")

	
	
@app.route("/tutorials/microsoft windows/"+TOPIC_DICT["Microsoft Windows"][0][1], methods=['GET', 'POST'])
def How_to_use_Linux_terminal_commands_in_Windows():
    return render_template("tutorials/Microsoft Windows/how-to-use-linux-terminal-commands-in-windows.html", curLink = TOPIC_DICT["Microsoft Windows"][0][1], curTitle=TOPIC_DICT["Microsoft Windows"][0][0], nextTitle = "None", curTopic = "Microsoft Windows", title = TOPIC_DICT["Microsoft Windows"][0][0], TOPIC_DICT = TOPIC_DICT)


@app.route("/tutorials/miscellaneous/"+TOPIC_DICT["Miscellaneous"][0][1], methods=['GET', 'POST'])
def How_to_install_Exodus_on_Kodi():
    return render_template("tutorials/Miscellaneous/how-to-install-exodus-on-kodi.html", curLink = TOPIC_DICT["Miscellaneous"][0][1], curTitle=TOPIC_DICT["Miscellaneous"][0][0], nextTitle=TOPIC_DICT["Miscellaneous"][1][0], curTopic = "Miscellaneous", title = TOPIC_DICT["Miscellaneous"][0][0], TOPIC_DICT = TOPIC_DICT, nextLink=TOPIC_DICT["Miscellaneous"][1][1])
	
@app.route("/tutorials/miscellaneous/"+TOPIC_DICT["Miscellaneous"][1][1], methods=['GET', 'POST'])
def How_to_setup_DoD_CACPKI_on_Chrome_Ubunutu_Linux():
    return render_template("tutorials/Miscellaneous/how-to-setup-dod-cac-pki-on-chrome-ubuntu-linux.html", curLink = TOPIC_DICT["Miscellaneous"][1][1], curTitle=TOPIC_DICT["Miscellaneous"][1][0], nextTitle = TOPIC_DICT["Miscellaneous"][2][0], curTopic = "Miscellaneous", title = TOPIC_DICT["Miscellaneous"][1][0], TOPIC_DICT = TOPIC_DICT, nextLink=TOPIC_DICT["Miscellaneous"][2][1])


@app.route("/tutorials/miscellaneous/"+TOPIC_DICT["Miscellaneous"][2][1], methods=['GET', 'POST'])
def Best_website_to_stream_live_sports():
    return render_template("tutorials/Miscellaneous/best-website-to-stream-live-sports.html", curLink = TOPIC_DICT["Miscellaneous"][2][1], curTitle=TOPIC_DICT["Miscellaneous"][2][0], curTopic = "Miscellaneous", title = TOPIC_DICT["Miscellaneous"][2][0], TOPIC_DICT = TOPIC_DICT, nextTitle= "None")


@app.route("/tutorials/java/"+TOPIC_DICT["Java"][0][1], methods=['GET', 'POST'])
def Hello_World_in_Java():
    return render_template("tutorials/Java/hello-world-in-java.html", curLink = TOPIC_DICT["Java"][0][1], curTitle=TOPIC_DICT["Java"][0][0], nextTitle =TOPIC_DICT["Java"][1][0], curTopic = "Java", title = TOPIC_DICT["Java"][0][0], TOPIC_DICT = TOPIC_DICT, nextLink=TOPIC_DICT["Java"][1][1])


@app.route("/tutorials/java/"+TOPIC_DICT["Java"][1][1], methods=['GET', 'POST'])
def Public_Private_Protected():
    return render_template("tutorials/Java/public-private-protected.html", curLink = TOPIC_DICT["Java"][1][1], curTitle=TOPIC_DICT["Java"][1][0], curTopic = "Java", title = TOPIC_DICT["Java"][1][0], TOPIC_DICT = TOPIC_DICT, nextTitle=TOPIC_DICT["Java"][2][0], nextLink=TOPIC_DICT["Java"][2][1])

@app.route("/tutorials/java/"+TOPIC_DICT["Java"][2][1], methods=['GET', 'POST'])
def Java_User_Input():
    return render_template("tutorials/Java/user-input.html", curLink = TOPIC_DICT["Java"][2][1], curTitle=TOPIC_DICT["Java"][2][0], curTopic = "Java", title = TOPIC_DICT["Java"][2][0], TOPIC_DICT = TOPIC_DICT, nextTitle=TOPIC_DICT["Java"][3][0], nextLink=TOPIC_DICT["Java"][3][1])

@app.route("/tutorials/java/"+TOPIC_DICT["Java"][3][1], methods=['GET', 'POST'])
def Printing_with_Stringoutformat():
    return render_template("tutorials/Java/printing-with-string-format.html", curLink = TOPIC_DICT["Java"][3][1], curTitle=TOPIC_DICT["Java"][3][0], curTopic = "Java", title = TOPIC_DICT["Java"][3][0], TOPIC_DICT = TOPIC_DICT, nextTitle= TOPIC_DICT["Java"][4][0], nextLink=TOPIC_DICT["Java"][4][1])


@app.route("/tutorials/java/"+TOPIC_DICT["Java"][4][1], methods=['GET', 'POST'])
def Java_Classes_and_Objects():
    return render_template("tutorials/Java/classes-and-objects.html", curLink = TOPIC_DICT["Java"][4][1], curTitle=TOPIC_DICT["Java"][4][0], curTopic = "Java", title = TOPIC_DICT["Java"][4][0], TOPIC_DICT = TOPIC_DICT, nextTitle=TOPIC_DICT["Java"][5][0], nextLink=TOPIC_DICT["Java"][5][1])

@app.route("/tutorials/java/"+TOPIC_DICT["Java"][5][1], methods=['GET', 'POST'])
def Class_inheritance():
    return render_template("tutorials/Java/class-inheritance.html", curLink = TOPIC_DICT["Java"][5][1], curTitle=TOPIC_DICT["Java"][5][0], curTopic = "Java", title = TOPIC_DICT["Java"][5][0], TOPIC_DICT = TOPIC_DICT, nextTitle=TOPIC_DICT["Java"][6][0], nextLink=TOPIC_DICT["Java"][6][1])

@app.route("/tutorials/java/"+TOPIC_DICT["Java"][6][1], methods=['GET', 'POST'])
def Dynamic_Arrays_using_ArrayList():
    return render_template("tutorials/Java/dynamic-arrays-using-arraylist.html", curLink = TOPIC_DICT["Java"][6][1], curTitle=TOPIC_DICT["Java"][6][0], curTopic = "Java", title = TOPIC_DICT["Java"][6][0], TOPIC_DICT = TOPIC_DICT, nextTitle= TOPIC_DICT["Java"][7][0], nextLink=TOPIC_DICT["Java"][7][1])


@app.route("/tutorials/java/"+TOPIC_DICT["Java"][7][1], methods=['GET', 'POST'])
def Queues():
    return render_template("tutorials/Java/queues.html", curLink = TOPIC_DICT["Java"][7][1], curTitle=TOPIC_DICT["Java"][7][0], curTopic = "Java", title = TOPIC_DICT["Java"][7][0], TOPIC_DICT = TOPIC_DICT, nextTitle=TOPIC_DICT["Java"][8][0], nextLink=TOPIC_DICT["Java"][8][1])

@app.route("/tutorials/java/"+TOPIC_DICT["Java"][8][1], methods=['GET', 'POST'])
def Exception_Handling():
    return render_template("tutorials/Java/exception-handling.html", curLink = TOPIC_DICT["Java"][8][1], curTitle=TOPIC_DICT["Java"][8][0], curTopic = "Java", title = TOPIC_DICT["Java"][8][0], TOPIC_DICT = TOPIC_DICT, nextTitle= "None")

@app.route("/tutorials/perl/"+TOPIC_DICT["Perl"][0][1], methods=['GET', 'POST'])
def Hello_World_in_Perl():
    return render_template("tutorials/Perl/hello-world-in-perl.html", curLink = TOPIC_DICT["Perl"][0][1], curTitle=TOPIC_DICT["Perl"][0][0], curTopic = "Perl", title = TOPIC_DICT["Perl"][0][0], TOPIC_DICT = TOPIC_DICT, nextTitle=TOPIC_DICT["Perl"][1][0], nextLink=TOPIC_DICT["Perl"][1][1])


@app.route("/tutorials/perl/"+TOPIC_DICT["Perl"][1][1], methods=['GET', 'POST'])
def How_to_store_information_in_variables():
    return render_template("tutorials/Perl/how-to-store-information-in-variables.html", curLink = TOPIC_DICT["Perl"][1][1], curTitle=TOPIC_DICT["Perl"][1][0], curTopic = "Perl", title = TOPIC_DICT["Perl"][1][0], TOPIC_DICT = TOPIC_DICT, nextTitle=TOPIC_DICT["Perl"][2][0], nextLink=TOPIC_DICT["Perl"][2][1])

@app.route("/tutorials/perl/"+TOPIC_DICT["Perl"][2][1], methods=['GET', 'POST'])
def Storing_User_Input_Perl():
    return render_template("tutorials/Perl/storing-user-input.html", curLink = TOPIC_DICT["Perl"][2][1], curTitle=TOPIC_DICT["Perl"][2][0], curTopic = "Perl", title = TOPIC_DICT["Perl"][2][0], TOPIC_DICT = TOPIC_DICT, nextTitle=TOPIC_DICT["Perl"][3][0], nextLink=TOPIC_DICT["Perl"][3][1])

@app.route("/tutorials/perl/"+TOPIC_DICT["Perl"][3][1], methods=['GET', 'POST'])
def While_Loop():
    return render_template("tutorials/Perl/while-loop.html", curLink = TOPIC_DICT["Perl"][3][1], curTitle=TOPIC_DICT["Perl"][3][0], curTopic = "Perl", title = TOPIC_DICT["Perl"][3][0], TOPIC_DICT = TOPIC_DICT, nextTitle= TOPIC_DICT["Perl"][4][0], nextLink=TOPIC_DICT["Perl"][4][1])

@app.route("/tutorials/perl/"+TOPIC_DICT["Perl"][4][1], methods=['GET', 'POST'])
def For_Loop():
    return render_template("tutorials/Perl/for-loop.html", curLink = TOPIC_DICT["Perl"][4][1], curTitle=TOPIC_DICT["Perl"][4][0], curTopic = "Perl", title = TOPIC_DICT["Perl"][4][0], TOPIC_DICT = TOPIC_DICT, nextTitle=TOPIC_DICT["Perl"][5][0], nextLink=TOPIC_DICT["Perl"][5][1])


@app.route("/tutorials/perl/"+TOPIC_DICT["Perl"][5][1], methods=['GET', 'POST'])
def Perl_Arrays():
    return render_template("tutorials/Perl/arrays.html", curLink = TOPIC_DICT["Perl"][5][1], curTitle=TOPIC_DICT["Perl"][5][0], curTopic = "Perl", title = TOPIC_DICT["Perl"][5][0], TOPIC_DICT = TOPIC_DICT, nextTitle=TOPIC_DICT["Perl"][6][0], nextLink=TOPIC_DICT["Perl"][6][1])


@app.route("/tutorials/perl/"+TOPIC_DICT["Perl"][6][1], methods=['GET', 'POST'])
def String_Interpolation():
    return render_template("tutorials/Perl/string-interpolation.html", curLink = TOPIC_DICT["Perl"][6][1], curTitle=TOPIC_DICT["Perl"][6][0], curTopic = "Perl", title = TOPIC_DICT["Perl"][6][0], TOPIC_DICT = TOPIC_DICT, nextTitle= "None")



@app.route("/tutorials/ruby/"+TOPIC_DICT["Ruby"][0][1], methods=['GET', 'POST'])
def Hello_World_in_Ruby():
    return render_template("tutorials/Ruby/hello-world-in-ruby.html", curLink = TOPIC_DICT["Ruby"][0][1], curTitle=TOPIC_DICT["Ruby"][0][0], curTopic = "Ruby", title = TOPIC_DICT["Ruby"][0][0], TOPIC_DICT = TOPIC_DICT, nextTitle="None")



	
@app.route("/blog/"+BLOG_TOPIC_DICT["blog"][0][1], methods=['GET', 'POST'])
def Programming_in_Python():
    return render_template("blog/programming-in-python.html", curLink = BLOG_TOPIC_DICT["blog"][0][1], curTitle=BLOG_TOPIC_DICT["blog"][0][0], curTopic = "blog", title = BLOG_TOPIC_DICT["blog"][0][0], BLOG_TOPIC_DICT = BLOG_TOPIC_DICT, TUTORIAL_CAT = TUTORIAL_CAT, nextTitle= "None")

@app.route('/robots.txt')
@app.route('/sitemap.xml')
@app.route('/BingSiteAuth.xml')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
