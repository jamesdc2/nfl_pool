import csv

from pool import Team

class Standings:
    def from_csv(self, filename):
        self.teams = []

        with open(filename, 'r') as csv_file:
            csv_data = csv.DictReader(csv_file, skipinitialspace=True)

            for row in csv_data:
                self.teams.append(Team(row))
                
        return self

    def all_teams(self):
        return self.teams
