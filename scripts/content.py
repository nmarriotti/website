def TutorialCategories():
    TUTORIAL_CAT = {"Types":[["Python","/tutorials/python","p-1.png"]]}

    return TUTORIAL_CAT

def Content():
    TOPIC_DICT = {"Python":[["Hello World!","hello-world"]]}

    return TOPIC_DICT





if __name__ == "__main__":
    x = Content()

    print(x["Python"])

    for each in x["Python"]:
        print(each[1])
