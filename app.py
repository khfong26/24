import flask 
from flask import jsonify, session
from helpers import get_four, share_cards # Import get_four instead of draw_card

app = flask.Flask(__name__)
app.secret_key = "super secret key" 

@app.route("/")
def index():
    return flask.render_template("index.html")

@app.route("/start")
def start():
    session['cards'] = get_four() # Cleaned up!
    print("started game")
    return jsonify({"cards": session['cards']})

@app.route("/next")
def next():
    session['cards'] = get_four() # Cleaned up!
    return jsonify({"cards": session['cards']})

@app.route("/share")
def share():
    print("sharing game")
    return jsonify({"cards": share_cards()})

if __name__ == "__main__":
    app.run(debug=True)