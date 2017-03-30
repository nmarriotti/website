from content import BlogContent
import os

BLOG_TOPIC_DICT = BlogContent()

HTML_TEMPLATE = """
{% extends "blog-view-master.html" %}
{% block content %}

<h6>Posted on DATEPOSTED</h6>

    {% if "STATUS" != "none" %}
        <div class="photo">
        	<img src="{{ url_for('static', filename='assets/img/blog/IMAGEFILENAME') }}" alt="IMAGEFILENAME">
        </div>
    {% endif %}

	  <div class="embed-responsive embed-responsive-16by9">VIDEO EMBED</div>

	  <p></p>
	  <p></p>
      <p></p>
	  <p></p>
	  <p></p>

{% endblock %}


"""

for each_topic in BLOG_TOPIC_DICT:
    print(each_topic)
    os.makedirs(each_topic)

    for eachele in BLOG_TOPIC_DICT[each_topic]:
        try:

            filename = (eachele[1]+'.html').replace("/","")
            print(filename)
            savePath = each_topic+'/'+filename

            saveData = (HTML_TEMPLATE.replace("%s",each_topic).replace("IMAGEFILENAME", eachele[4]).replace("STATUS", eachele[4]).replace("DATEPOSTED", eachele[2]))

            template_save = open(savePath,"w")
            template_save.write(saveData)
            template_save.close()
        except Exception as e:
            print(str(e))
