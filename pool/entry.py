class Entry:
    def __init__(self,opts):
        self.name = opts['name']
        self.teams = opts['teams']
        self.total_wins = opts['total_wins']
        self.total_losses = opts['total_losses']
        self.pf = opts['pf']
        self.pa = opts['pa']
        self.diff = opts['diff']
