import csv
from functools import reduce
from pool import Entry

class EntryList:
    def from_csv(self,filename):
        self.entries = []

        with open(filename, 'r') as csv_file:
            csv_data = csv.DictReader(csv_file,skipinitialspace=True)

            for row in csv_data:
                teams = {
                        row['team_a'].upper():row['team_a_wins'],
                        row['team_b'].upper():row['team_b_wins'],
                        row['team_c'].upper():row['team_c_wins']
                        }
                
                total_wins = reduce(lambda x, y: int(x) + int(y), teams.values())
                
                self.entries.append(Entry({
                    "name":row['name'],
                    "teams":teams,
                    "total_wins":total_wins
                }))
        return self
