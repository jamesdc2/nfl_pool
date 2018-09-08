from flask import Flask,render_template
app = Flask(__name__)

from pool import EntryList

entrylist = EntryList().from_csv('data/entries.csv')

@app.route('/')
def index():
    leaderboard = sorted(entrylist.entries, key=lambda entry: entry.total_wins,reverse=True)	
    return render_template('leaderboard.html',leaderboard=enumerate(leaderboard))


if __name__ == "__main__":
        app.debug = True
        app.run()
