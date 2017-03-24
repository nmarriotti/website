from content import Content
import os

TOPIC_DICT = Content()

HTML_TEMPLATE = """
{% extends "tutorial-master.html" %}
{% block content %}
<!--       <pre class="prettyprint">              width="750" height="423"    -->

	  <div class="embed-responsive embed-responsive-16by9"><iframe width="560" height="315" src="https://www.youtube.com/embed/OIuXVZuHXXo" frameborder="0" allowfullscreen></iframe></div>

	  <p></p>
	  <p></p>
	  <p></p>
	  <p></p>


	  <kbd data-toggle="collapse" data-target="#consoleinfo" aria-expanded="false" aria-controls="consoleinfo">console</kbd>

		<div class="collapse" id="consoleinfo">
		  <div class="well">
			<p>When someone refers to "the console," they are referring to where information from your program is ouput. You will see an example of "output to console" below. If you want this message to go away, just click again on the "console" button that you originally clicked on.</p>
		  </div>
		</div>



		<div class="row">
      <pre class="brush: py;">
def HelloWorld():
    print("Hello World")
  </pre>
		<div class="col l6">
<p>EXPLANATION</p></div></div>



<div class="post-pagination">
   {% if nextTitle != "None" %}
  <a title="{{nextTitle}}" href="{{nextLink}}" class="btn btn-color-hover hover-animate next"> Next Tutorial: {{nextTitle}}</a>
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
