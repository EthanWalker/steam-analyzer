from steam import (
    get_avatar,
    get_friends,
    get_games,
    get_persona,
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
    username = get_persona(steam_id)
    game_count = get_games(steam_id)["count"]
    friends_count = len(get_friends(steam_id))
    avatar = get_avatar(steam_id)
    context = {
        "username": username,
        "game_count": game_count,
        "friends_count": friends_count,
        "avatar": avatar,
    }
    return render_template("index.html", **context)



app.run(debug = True, port = 8080, host = '127.0.0.1')