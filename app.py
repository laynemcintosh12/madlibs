from flask import Flask, render_template, request
from stories import story
from random import randint


app = Flask(__name__)


@app.route("/")
def home_page():
    form_var = story.prompts
    return render_template("base.html", form_var=form_var)


@app.route("/story")
def gen_story():
    my_story = story.generate(request.args)
    return render_template("story.html", my_story=my_story)