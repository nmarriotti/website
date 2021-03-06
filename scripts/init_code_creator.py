#!/usr/bin/python
from content import Content

TOPIC_DICT = Content()

FUNC_TEMPLATE = '''

@app.route("/tutorials/CURRENTTOPICLOW/"+TOPIC_DICT["CURRENTTOPIC"][CURRENTINDEX][1], methods=['GET', 'POST'])
def CURRENTTITLE():
    return render_template("tutorials/CURRENTTOPIC/CURRENTHTML", curLink = TOPIC_DICT["CURRENTTOPIC"][CURRENTINDEX][1], curTitle=TOPIC_DICT["CURRENTTOPIC"][CURRENTINDEX][0],  nextLink = TOPIC_DICT["CURRENTTOPIC"][NEXTINDEX][1], nextTitle = TOPIC_DICT["CURRENTTOPIC"][NEXTINDEX][0], curTopic = "CURRENTTOPIC", title = TOPIC_DICT["CURRENTTOPIC"][CURRENTINDEX][0], TOPIC_DICT = TOPIC_DICT)

'''

FUNC_TEMPLATE_LAST = '''

@app.route("/tutorials/CURRENTTOPICLOW/"+TOPIC_DICT["CURRENTTOPIC"][CURRENTINDEX][1], methods=['GET', 'POST'])
def CURRENTTITLE():
    return render_template("tutorials/CURRENTTOPIC/CURRENTHTML", curLink = TOPIC_DICT["CURRENTTOPIC"][CURRENTINDEX][1], curTitle=TOPIC_DICT["CURRENTTOPIC"][CURRENTINDEX][0], curTopic = "CURRENTTOPIC", title = TOPIC_DICT["CURRENTTOPIC"][CURRENTINDEX][0], TOPIC_DICT = TOPIC_DICT, nextTitle= "None")

'''

for each_topic in TOPIC_DICT:
    #print(each_topic)

    index_counter = 0
    for eachele in TOPIC_DICT[each_topic]:
        try:
            CURRENTHTML = (eachele[1]+'.html').replace("/","")
            CURRENTTOPIC = each_topic
            CURRENTTITLE = eachele[0].replace("-","_").replace(" ","_").replace(",","").replace("/","").replace(")","").replace("(","").replace(".","").replace("!","").replace(":","-").replace("'","")
            CURRENTINDEX = str(index_counter)
            try:
                if eachele[index_counter]:
                    NEXTINDEX = str(index_counter+1)   
                    print( FUNC_TEMPLATE.replace("CURRENTTOPICLOW",CURRENTTOPIC.lower()).replace("CURRENTTOPIC",CURRENTTOPIC).replace("CURRENTINDEX",CURRENTINDEX).replace("CURRENTTITLE",CURRENTTITLE).replace("CURRENTHTML",CURRENTHTML).replace("NEXTINDEX",NEXTINDEX) )
            except:
                print( FUNC_TEMPLATE_LAST.replace("CURRENTTOPICLOW",CURRENTTOPIC.lower()).replace("CURRENTTOPIC",CURRENTTOPIC).replace("CURRENTINDEX",CURRENTINDEX).replace("CURRENTTITLE",CURRENTTITLE).replace("CURRENTHTML",CURRENTHTML) )

            index_counter += 1
 
        except Exception as e:
            print(str(e))
