from content import BlogContent

BLOG_TOPIC_DICT = BlogContent()

FUNC_TEMPLATE = '''

@app.route("/blog/"+TOPIC_DICT["CURRENTTOPIC"][CURRENTINDEX][1], methods=['GET', 'POST'])
def CURRENTTITLE():
    return render_template("CURRENTTOPIC/CURRENTHTML", curLink = BLOG_TOPIC_DICT["CURRENTTOPIC"][CURRENTINDEX][1], curTitle=BLOG_TOPIC_DICT["CURRENTTOPIC"][CURRENTINDEX][0],  nextLink = BLOG_TOPIC_DICT["CURRENTTOPIC"][NEXTINDEX][1], nextTitle = BLOG_TOPIC_DICT["CURRENTTOPIC"][NEXTINDEX][0], curTopic = "CURRENTTOPIC", title = BLOG_TOPIC_DICT["CURRENTTOPIC"][CURRENTINDEX][0], BLOG_TOPIC_DICT = BLOG_TOPIC_DICT)

'''

FUNC_TEMPLATE_LAST = '''

@app.route("/CURRENTTOPICLOW/"+BLOG_TOPIC_DICT["CURRENTTOPIC"][CURRENTINDEX][1], methods=['GET', 'POST'])
def CURRENTTITLE():
    return render_template("CURRENTTOPIC/CURRENTHTML", curLink = BLOG_TOPIC_DICT["CURRENTTOPIC"][CURRENTINDEX][1], curTitle=BLOG_TOPIC_DICT["CURRENTTOPIC"][CURRENTINDEX][0], curTopic = "CURRENTTOPIC", title = BLOG_TOPIC_DICT["CURRENTTOPIC"][CURRENTINDEX][0], BLOG_TOPIC_DICT = BLOG_TOPIC_DICT, nextTitle= "None")

'''

for each_topic in BLOG_TOPIC_DICT:
    #print(each_topic)

    index_counter = 0
    for eachele in BLOG_TOPIC_DICT[each_topic]:
        try:
            CURRENTHTML = (eachele[1]+'.html').replace("/","")
            CURRENTTOPIC = each_topic
            CURRENTTITLE = eachele[0].replace("-","_").replace(" ","_").replace(",","").replace("/","").replace(")","").replace("(","").replace(".","").replace("!","").replace(":","-").replace("'","")
            CURRENTINDEX = str(index_counter)
            index_counter += 1
            try:
                if eachele[index_counter]:
                    print( FUNC_TEMPLATE.replace("CURRENTTOPICLOW",CURRENTTOPIC.lower()).replace("CURRENTTOPIC",CURRENTTOPIC).replace("CURRENTINDEX",CURRENTINDEX).replace("CURRENTTITLE",CURRENTTITLE).replace("CURRENTHTML",CURRENTHTML).replace("NEXTINDEX",NEXTINDEX) )
            except:
                print( FUNC_TEMPLATE_LAST.replace("CURRENTTOPICLOW",CURRENTTOPIC.lower()).replace("CURRENTTOPIC",CURRENTTOPIC).replace("CURRENTINDEX",CURRENTINDEX).replace("CURRENTTITLE",CURRENTTITLE).replace("CURRENTHTML",CURRENTHTML) )


        except Exception as e:
            print(str(e))
