import flask
import os 
import random
import requests
import json
import tweepy
import twit
import spoo
from flask import render_template

    
app = flask.Flask(__name__)

@app.route('/')
def main():
    recipe = spoo.get_recipe_data()
    tweet = twit.get_tweet() 
    
    return render_template('index.html', recipe_data = recipe, twitter_data = tweet, len = len(recipe.ingredients))
    
app.run(
    port = int(os.getenv('PORT')),
    host = os.getenv('IP','0.0.0.0'),
    debug = True
)