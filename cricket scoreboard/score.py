class Team:
    def __init__(self, name, batting_order=None, score=0, wickets=0, over=0.0, extra=0):
        if batting_order is None:
            self.batting_order = []
        self.name = name
        self.score = score
        self.wickets = wickets
        self.over = over
        self.extra = extra

    def get_score(self):
        #optimize this code
        score = 0
        for _player in self.batting_order:
            score += _player.score
        self.score = score + self.extra
        return self.score

    # def set_score(self, val):
    #     self.score += val

    def get_wickets(self):
        return self.wickets


class Player:
    def __init__(self, name, team, fours=0, sixes=0, balls=0, score=0, not_out=False,
                 currently_playing=False, strike_rate=0.0, run_concede=0, wickets=0, overs=0.0, extra=0):
        self.name = name
        self.team = team
        self.score = score
        self.fours = fours
        self.sixes = sixes
        self.balls = balls
        self.not_out = not_out
        self.currently_playing = currently_playing  # ["___"
        self.strike_rate = strike_rate
        self.run_concede = run_concede
        self.wickets = wickets
        self.overs = overs
        self.extra = extra

# Batsman and bowler class can be extended

    def get_strike_rate(self):
        return round((self.score / self.balls)*100, 2) if self.balls else 0.0
