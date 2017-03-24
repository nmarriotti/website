def TutorialCategories():
    TUTORIAL_CAT = {"Types":[["Python","/tutorials/python","p-1.png"],
["Visual Basic","/tutorials/vb","visual_studio.png"]]}

    return TUTORIAL_CAT

def Content():
    TOPIC_DICT = {"Python":[["Hello World!","/hello-world"],
    ["If/Else Statement","/if-else-statement"],
    ["For Loop","/for-loop"],
    ["While Loop","/while-loop"]]}

    return TOPIC_DICT





if __name__ == "__main__":
    x = Content()

    print(x["Python"])

    for each in x["Python"]:
        print(each[1])
