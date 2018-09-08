from flask import Flask,render_template
application = Flask(__name__)

from pool import Leaderboard

leaderboard = Leaderboard().from_csv('data/entries.csv','data/nfl_standings_week1.csv')

@application.route('/')
def index():
    entries = sorted(leaderboard.entries, key=lambda e: (-e.total_wins,e.total_losses,-e.diff))
    return render_template('leaderboard.html',leaderboard=enumerate(entries))


if __name__ == "__main__":
        application.run()