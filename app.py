from steam import (
    get_avatar,
    get_friends,
    get_games,
    get_persona,
    get_top_game_counts,
    get_top_games,
    make_pie_chart,
    make_hbar_chart,
    get_playtime,
)
from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico')

@app.route('/jumbobg.jpg')
def jumbobg():
    return send_from_directory(os.path.join(app.root_path, 'static'),'jumbobg.jpg')

@app.route('/style.css')
def style():
    return send_from_directory(os.path.join(app.root_path, 'static'),'style.css')



@app.route('/')
@app.route('/<steam_id>')
def index(steam_id="76561197960435530"):
    if len(steam_id) > 17:
        return render_template("404.html")
    username = get_persona(steam_id)
    game_count = get_games(steam_id)["count"]
    top_game_counts = get_top_game_counts(steam_id)
    top_game_counts_chart = make_hbar_chart(top_game_counts, 'Top 5 friend game counts')
    top_games = get_top_games(steam_id)
    top_games_chart = make_pie_chart(top_games, 'Top 5 games by playtime (in hrs)')
    friends_count = len(get_friends(steam_id))
    avatar = get_avatar(steam_id)
    playtime = get_playtime(steam_id)
    context = {
        "username": username,
        "game_count": game_count,
        "friends_count": friends_count,
        "avatar": avatar,
        "top_game_counts": top_game_counts,
        "top_games": top_games,
        "top_games_chart": top_games_chart,
        "top_game_counts_chart": top_game_counts_chart,
        "playtime": playtime,
    }
    return render_template("index.html", **context)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

app.run(debug = True, port = 8080, host = '127.0.0.1')