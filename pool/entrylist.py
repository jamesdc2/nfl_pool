import csv

from pool import Entry

class EntryList:
    def from_csv(self,filename):
        self.entries = []

        with open(filename, 'r') as csv_file:
            csv_data = csv.DictReader(csv_file,skipinitialspace=True)

            for row in csv_data:
                teams = {row['team_a'],row['team_b'],row['team_c']}
                self.entries.append(Entry({"name":row['name'],"teams":teams}))

        return self
