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
    TOPIC_DICT = {"Python":[["Hello World!","hello-world"]],
    "C++":[["Hello World!","hello-world"]]}

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
