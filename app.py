from steam import (
    get_avatar,
    get_friends,
    get_games,
    get_persona,
    #get_top_game_count,
)
from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico')


@app.route('/')
@app.route('/<steam_id>')
def index(steam_id="76561197960435530"):
    if len(steam_id) > 17:
        return render_template("404.html")
    username = get_persona(steam_id)
    game_count = get_games(steam_id)["count"]
    #top_game_count = get_top_game_count(steam_id)
    friends_count = len(get_friends(steam_id))
    avatar = get_avatar(steam_id)
    context = {
        "username": username,
        "game_count": game_count,
        "friends_count": friends_count,
        "avatar": avatar,
        #"top_persona": top_game_count[0],
        #"top_game_count": top_game_count[1],
    }
    return render_template("index.html", **context)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

app.run(debug = True, port = 8080, host = '127.0.0.1')