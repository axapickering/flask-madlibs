from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story, excited_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


STORY_NAMES = {
    "excited" : excited_story,
    "silly" : silly_story
}


@app.get("/")
def home_page():
    '''shows the homepage, allows user to pick a story'''
    template = render_template("base.html")

    return template


@app.get("/questions")
def show_questions():
    ''' Shows the madlib questions form'''
    story_name = request.args['story_name']
    inputs = STORY_NAMES[story_name].prompts
    template = render_template("questions.html",inputs=inputs,story_name=story_name)

    return template


@app.get("/results")
def show_results():
    ''' Displays the results page including the story text'''
    story_name = request.args.get('story_name')

    story = silly_story.get_result_text(request.args)
    template = render_template("results.html",story=story)

    return template
