def TutorialCategories():
    TUTORIAL_CAT = {"Types":[["Python","/tutorials/python","p-1.png"]]}

    return TUTORIAL_CAT

def Content():
    TOPIC_DICT = {"Python":[["Hello World!","hello-world"]]}

    return TOPIC_DICT

def BlogContent():
	                            # TITLE            URL                DATE         description                                                      image
    BLOG_TOPIC_DICT = {"blog":[["First Blog Post","first-blog-post", "12/25/2017", "This is where the description of the blog entry needs to go.", "post-1.png"],
    ["Second Blog Post","first-blog-post", "12/25/2017", "This is where the description of the blog entry needs to go.", "post-1.png"]]}

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
