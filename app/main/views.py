from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_source, get_article


@main.route("/")
def index():
    '''
    View root page function that returns the index page and its data
    '''
    entertainment = get_source('entertainment')
    business = get_source('business')
    general = get_source('general')
    health = get_source('health')
    science = get_source('science')
    sports = get_source('sports')
    technology = get_source('technology')

    
    title="Home-Welcome to NEWS sources Website"
    return render_template('index.html', entertainment = entertainment, business = business, general = general, health = health, science = science, sports =sports, technology = technology, title = title)


@main.route('/source/<id>')
def get_articles(id):
    articles = get_article(id)
    return render_template('articles.html', articles = articles)