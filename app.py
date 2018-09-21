from flask import Flask,render_template,jsonify
from pool import Leaderboard, Standings
import os
import time

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


url = "https://www.pro-football-reference.com/years/2018/index.htm"
teams = Standings().fetch(url)
leaderboard = Leaderboard().from_csv('data/entries.csv',teams)

@app.route('/')
def index():
    last_mod = teams.last_update.strftime("%c") 

    entries = sorted(leaderboard.entries, key=lambda e: (-e.total_wins,e.total_losses,-e.diff))
    return render_template('leaderboard.html',leaderboard=enumerate(entries),last_mod=last_mod)

@app.route('/standings')
def standings():
    return jsonify(teams.as_json())

@app.route('/standings/update')
def update_standings():
    teams = Standings().fetch(url)
    leaderboard = Leaderboard().from_csv('data/entries.csv', teams)
    return jsonify({'status':'successsful'})

if __name__ == "__main__":
    app.run()
