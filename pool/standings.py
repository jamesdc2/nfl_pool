import csv
import datetime
from selectolax.parser import HTMLParser
from urllib import request
from pool import Team

class Standings:

    def __init__(self):
    
        self.abbrev = {
            "Arizona Cardinals": "ARI",
            "Atlanta Falcons": "ATL",
            "Baltimore Ravens": "BAL",
            "Buffalo Bills": "BUF",
            "Carolina Panthers": "CAR",
            "Cleveland Browns": "CLE",
            "Chicago Bears": "CHI",
            "Cincinnati Bengals": "CIN",
            "Dallas Cowboys": "DAL",
            "Denver Broncos": "DEN",
            "Detroit Lions": "DET",
            "Green Bay Packers": "GB",
            "Houston Texans": "HOU",
            "Indianapolis Colts": "IND",
            "Jacksonville Jaguars": "JAC",
            "Kansas City Chiefs": "KC",
            "Los Angeles Chargers": "LAC",
            "Los Angeles Rams": "LAR",
            "Miami Dolphins": "MIA",
            "Minnesota Vikings": "MIN",
            "New England Patriots": "NE",
            "New Orleans Saints": "NO",
            "New York Giants": "NYG",
            "New York Jets": "NYJ",
            "Oakland Raiders": "OAK",
            "Philadelphia Eagles": "PHI",
            "Pittsburgh Steelers": "PIT",
            "San Francisco 49ers": "SF",
            "Seattle Seahawks": "SEA",
            "Tampa Bay Buccaneers": "TB",
            "Tennessee Titans": "TEN",
            "Washington Redskins": "WAS"
        }

        self.teams = {}
    
    def from_csv(self, filename):

        with open(filename, 'r') as csv_file:
            csv_data = csv.DictReader(csv_file, skipinitialspace=True)
            for row in csv_data:
                opts = {'NAME':row['NAME'],'W':row['W'],'L':row['L'],'PF':row['PF'],'PA':row['PA'],'DIFF':row['DIFF']}
                self.teams[row['TEAM']] = Team(opts)
                
        return self

    def fetch(self,url):
        url = "https://www.pro-football-reference.com/years/2018/index.htm"
        selector = "*[data-stat]:not(*.poptip):not(*[data-stat=onecell])"

        html = request.urlopen(url).read()
        self.last_update = datetime.datetime.now()

        cells = HTMLParser(html).css(selector)

        for i in range(0,len(cells)-1,13):
            opts = {'NAME':cells[i].text(),
                    'W':cells[i+1].text(),
                    'L':cells[i+2].text(),
                    'PF': cells[i+5].text(),
                    'PA': cells[i+6].text(),
                    'DIFF': cells[i+7].text()
                    }
            self.teams[self.abbrev[cells[i].text()]] = Team(opts)

        return self

    def as_json(self):
        return list(map(lambda x: x.__json__(), self.teams.values()))

    def all_teams(self):
        return self.teams
