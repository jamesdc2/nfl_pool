import csv
from functools import reduce
from pool import Entry
from pool import Standings

class Leaderboard:
    def from_csv(self,filename,standings_filename):
        standings = Standings().from_csv(standings_filename)
        self.entries = []

        with open(filename, 'r') as csv_file:
            csv_data = csv.DictReader(csv_file,skipinitialspace=True)

            for row in csv_data:
                teams = {
                        row['team_a'].upper():standings.teams[row['team_a'].upper()],
                        row['team_b'].upper():standings.teams[row['team_b'].upper()],
                        row['team_c'].upper():standings.teams[row['team_c'].upper()]
                }
                total_wins=total_losses=pf=pa=diff=0
                for name,team in teams.items(): 
                    total_wins += team.wins
                    total_losses += team.losses
                    pf += team.pf
                    pa += team.pa
                    diff += team.diff
                    
                self.entries.append(Entry({
                    "name":row['name'],
                    "teams":teams,
                    "total_wins":total_wins,
                    'total_losses':total_losses,
                    "pf":pf,
                    "pa":pa,
                    "diff":diff
                }))
        return self
