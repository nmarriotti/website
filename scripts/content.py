def TutorialCategories():
    TUTORIAL_CAT = {"Types":[["Python","/tutorials/python","p-1.png"],
    ["C","/tutorials/c","p-1.png"],
    ["C++","/tutorials/c++","p-1.png"],
    ["Java","/tutorials/java","p-1.png"],
    ["Visual Basic","/tutorials/visual basic","p-1.png"],
    ["Microsoft Windows","/tutorials/microsoft windows","p-1.png"],
    ["Miscellaneous","/tutorials/miscellaneous","p-1.png"]]}

    return TUTORIAL_CAT

def Content():
    TOPIC_DICT = {"Python":[["Getting Started with Python","getting-started-with-python"],
	["Creating a Hello World program in Python!","hello-world"],
    ["How to use variables","how-to-use-variables"],
    ["Functions","functions"],
    ["Using lists to store information","using-lists-to-store-information"],
    ["Storing information in dictionaries","storing-information-in-dictionaries"],
    ["Lambda Functions","lambda-functions"],
    ["If Statements","if-statements"],
    ["Loops","loops"]],
    "C":[["Hello World!","hello-world"],
    ["Printing variables with printf","printing-variables-with-printf"],
    ["Command Line Arguments","command-line-arguments"],
    ["User Input","user-input"],
    ["Creating Header Files","creating-header-files"],
    ["Structs","structs"],
    ["Union","union"],
    ["Switch Statement","switch-statement"],
    ["Writing Files","writing-files"],
    ["Reading Files","reading-files"],
    ["Functions","functions"]],
    "C++":[["Installing the C++ compiler and Code:Blocks IDE","installing-compiler-and-codeblocks-ide"],
    ["Creating a Hello World program in C++!","hello-world"],
    ["Getting user input and variables","user-input-and-variables"],
    ["Data Types","data-types"],
    ["Conditional Statements","conditional-statements"],
    ["Loops","loops"],
    ["How to create and use functions","how-to-create-and-use-functions"],
    ["Arrays","arrays"],
    ["Writing Files","writing-files"],
    ["Reading Files","reading-files"],
    ["Reading CSV Files","reading-csv-files"],
    ["Classes and Objects","classes-and-objects"],
    ["Pointers and References","pointers-and-references"]],
    "Microsoft Windows":[["How to use Linux terminal commands in Windows","how-to-use-linux-terminal-commands-in-windows"]],
    "Miscellaneous":[["How to install Exodus on Kodi","how-to-install-exodus-on-kodi"]],
    "Java":[["Hello World in Java","hello-world-in-java"]]}

    return TOPIC_DICT

def BlogContent():
	                            # TITLE            URL                DATE         description                                                      image
    BLOG_TOPIC_DICT = {"blog":[["Programming in Python","programming-in-python", "3/26/2017", "Just talking about what made me want to make this website and what kind of tutorials I am going to post in the future.", "none"]]}

    return BLOG_TOPIC_DICT



if __name__ == "__main__":
    x = Content()

    print(x["Python"])

    for each in x["Python"]:
        print(each[1])

    y = BlogContent()

    print(y["Blog"])

    for each in y["Blog"]:
    	print(each[1])
