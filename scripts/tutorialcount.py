from content import *

TOPIC_DICT = Content()
TUTORIAL_CAT = TutorialCategories()

def getCount():
    count = 0
    x = 0
    for key, value in TOPIC_DICT.items():
        for items in TOPIC_DICT[key]:
            count += 1
        x += 1


    return count
