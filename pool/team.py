class Team:
    def __init__(self,opts):
        self.name = opts['NAME']
        self.wins = int(opts['W'])
        self.losses = int(opts['L'])
        self.pf = int(opts['PF'])
        self.pa = int(opts['PA'])
        self.diff = int(opts['DIFF'])
