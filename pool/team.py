class Team:
    def __init__(self,opts):
        self.name = opts['NAME']
        self.wins = int(opts['W'])
        self.losses = int(opts['L'])
        self.pf = int(opts['PF'])
        self.pa = int(opts['PA'])
        self.diff = int(opts['DIFF'])
    
    def __repr__(self):
        return "[{0: <2}]{1: <20}({2}-{3})".format(self.name, \
                " ",
                self.wins, \
                self.losses)

    def __json__(self):
        return {
                self.name: {
                "wins": self.wins,
                "losses": self.losses,
                "points for": self.pf,
                "points against": self.pa,
                "points diff": self.diff }
        }
