from flask import Flask, render_template, request
from route.ghexception import githubApiError
from route.githubapi import repo_with_stars


app = Flask(__name__)


languages = ['Python', 'Javascript', 'Assembly']


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        selected_lang = languages
    elif request.method == 'POST':
        selected_lang = request.form.getlist("languages")
    results = repo_with_stars(selected_lang)
    return render_template('index.html', selected_lang=selected_lang, languages=languages, results=results)


@app.errorhandler(githubApiError)
def handle_api_error(error):
    return render_template('404.html', message=error)
