import markdown
from os import path
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    """Show the Readme"""
    with open(path.dirname(app.root_path) + '/README.md') as readme:
        content = readme.read()
        return markdown.markdown(content)