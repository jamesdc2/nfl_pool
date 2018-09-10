from flask import Flask,render_template
import os
import time
app = Flask(__name__)

from pool import Leaderboard

standings_file = 'data/nfl_standings_week1_3.csv'
leaderboard = Leaderboard().from_csv('data/entries.csv',standings_file)

@app.route('/')
def index():

    statbuf = os.stat(standings_file)
    last_mod = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(statbuf.st_mtime))

    entries = sorted(leaderboard.entries, key=lambda e: (-e.total_wins,e.total_losses,-e.diff))
    return render_template('leaderboard.html',leaderboard=enumerate(entries),last_mod=last_mod)


if __name__ == "__main__":
        app.run()
