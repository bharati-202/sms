class Team:
    def  __init__(self, name):
        self.name = name
        self.score = 0

    def __repr__(self):
        return self.name

class Match:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.winner = None

    def play_match(self):
        score1 = int(input(f"Enter score for {self.team1}: "))
        score2 = (int(input(f"Enter score for {self.team2}: ")))


        if score1 > score2:
            self.winner = self.team1
        else:
            self.winner = self.team2
        print(f"Winner: {self.winner}")

    def __repr__(self):
        return f"{self.team1} vs {self.team2}"

class Tournament:
    def __init__(self, teams):
        self.teams = [Team(name) for name in teams]
        self.poll_a = self.teams[:8]
        self.poll_b = self.teams[8:]
        self.matches_a = self.schedule_matches(self.poll_a)
        self.matches_b = self.schedule_matches(self.poll_b)

    def schedule_matches(self, poll):
        matches = []

        for i in range(len(poll)):
            for j in range(i + 1, len(poll)):
                matches.append(Match(poll[i], poll[j]))
        return matches

    def play_tournament(self, matches):
        standings = {}
        for match in matches:
            match.play_match()
            winner = match.winner
            if winner.name in standings:
                standings[winner.name] += 1
            else:
                standings[winner.name] = 1
        return standings

    def __repr__(self):
        return f"Tournament with {len(self.teams)} teams"

# Example usage:

teams = [f"team {i+1}" for i in range(16)]
tournament = Tournament(teams)
print("Poll a Matches: ")
for match in tournament.matches_a:
    print(match)

print("\nPoll B Matches: ")
for match in tournament.matches_b:
    print(match)

standing_a = tournament.play_tournament(tournament.matches_a)
standing_b = tournament.play_tournament(tournament.matches_b)

print("\nPoll A standings: ", standing_a)
print("Poll B Standing: ", standing_b)


