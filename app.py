from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


# wordlist = sillu_story.prompts


@app.route('/')
def generate_prompts():
    """Create input fields extracted from story instance prompts"""
    prompts = silly_story.prompts
    return render_template("questions.html", words_list=prompts)
