#!/usr/bin/python
from content import Content
import os

TOPIC_DICT = Content()

HTML_TEMPLATE = """
{% extends "tutorial-master.html" %}

{% block metatags %}
<meta name="keywords" content="KEYWORDS GO HERE" />
<meta name="description" content="DESCRIPTION GOES HERE" />
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1" />
{% endblock %}

{% block content %}


	  <div class="embed-responsive embed-responsive-16by9">VIDEO EMBED</div>

	  <p></p>
	  <p></p>


<pre class="line-numbers"><code class="language-python">
PYTHON CODE
</code></pre>

	  <p></p>
	  <p></p>
	  <p></p>
	  <p></p>


<pre class="command-line"><code class="language-bash">
COMMAND PROMPT CODE HERE
</code></pre>



<br>


<div class="post-pagination">
   {% if nextTitle != "None" %}
  <center><a title="{{nextTitle}}" href="{{nextLink}}" class="btn btn-color-hover hover-animate next"> Next Tutorial: {{nextTitle}}</a></center>
  {% else %}
  You've reached the last tutorial for now. Check back later for more.
  <a title="Home" href="/" class="btn btn-color-hover hover-animate">Home</a>
  {% endif %}
</div>


{% endblock %}


"""

for each_topic in TOPIC_DICT:
    print(each_topic)
    os.makedirs(each_topic)

    for eachele in TOPIC_DICT[each_topic]:
        try:

            filename = (eachele[1]+'.html').replace("/","")
            print(filename)
            savePath = each_topic+'/'+filename

            saveData = (HTML_TEMPLATE.replace("%s",each_topic))

            template_save = open(savePath,"w")
            template_save.write(saveData)
            template_save.close()
        except Exception as e:
            print(str(e))
