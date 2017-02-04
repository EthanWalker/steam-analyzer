from steam import (
    get_avatar,
    get_friends_list,
    get_game_list,
    get_persona_name,
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
    username = get_persona_name(steam_id)
    game_count = get_game_list(steam_id)["count"]
    friends_count = len(get_friends_list(steam_id))
    avatar = get_avatar(steam_id)
    context = {
        "username": username,
        "game_count": game_count,
        "friends_count": friends_count,
        "avatar": avatar,
    }
    return render_template("index.html", **context)



app.run(debug = True, port = 8080, host = '127.0.0.1')