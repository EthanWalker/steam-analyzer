from steam import *
from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/')
@app.route('/<steam_id>')
def index(steam_id="76561197960435530"):
    return render_template("index.html", steam_id=steam_id)



app.run(debug = True, port = 8080, host = '127.0.0.1')