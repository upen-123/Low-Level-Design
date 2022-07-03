from score import Team, Player
from util import process_a_over

if __name__ == '__main__':
    team_1 = Team(name="Team_1")
    team_2 = Team(name="Team_2")

    number_of_players = int(input("No. of players for each team:"))

    number_of_overs = int(input("No. of overs:"))

    print("Batting Order for Team 1:")

    for _ in range(number_of_players):
        player_name = input()
        P1 = Player(name=player_name, team=team_1)
        team_1.batting_order.append(P1)

    print("Batting Order for Team 2:")

    for _ in range(number_of_players):
        player_name = input()
        P1 = Player(name=player_name, team=team_2)
        team_2.batting_order.append(P1)

    for inning in range(1, 3):  # there are two innigs
        # team = team_1 if t == 1 else team_2
        team, bowling_team = (team_1, team_2) if inning == 1 else (team_2, team_1)

        strike_player, non_strike_player = team.batting_order[0], team.batting_order[1]
        strike_player.currently_playing, non_strike_player.currently_playing = True, True
        upcoming_player_no = 2

        print("Batting of {}".format(team.name))
        print("")
        print("Bowling by {}".format(bowling_team.name))

        index = 0
        while index < number_of_overs:
            print("Over_{}:".format(index + 1))
            bowler_name = input("Bowler Name:")

            bowler = next((x for x in bowling_team.batting_order if x.name == bowler_name), None)
            if not bowler:
                print("Please provide valid bowler Name.")
                continue

            balls_in_a_over = 6
            # process each over
            balls_in_a_over = process_a_over(team, strike_player, non_strike_player, upcoming_player_no,
                                             balls_in_a_over, number_of_players, team_1, team_2, bowler)

            exp = (1 if balls_in_a_over == 0 else (6 - balls_in_a_over) / 10)
            team.over += exp
            bowler.overs += exp

            print("Scorecard for {}:".format(team.name))
            print("Player", "Score", "4s", "6s", "Balls", "Strike Rate")

            for player in team.batting_order:
                if player.currently_playing:
                    print(player.name + "*", '\t', player.score, '\t', player.fours, '\t', player.sixes, '\t',
                          player.balls, '\t', player.get_strike_rate())
                    continue
                print(player.name + " ", '\t', player.score, '\t', player.fours, '\t', player.sixes, '\t', player.balls,
                      '\t',
                      player.get_strike_rate())

            print('')

            print("Scorecard for Bowling {}:".format(bowling_team.name))
            print("Player", "Run_Concede", "Overs", "Wickets")
            for bowler in bowling_team.batting_order:
                if bowler.overs:
                    print(bowler.name, '\t', '\t', bowler.run_concede, '\t', '\t', bowler.overs, '\t', bowler.wickets)

            print("\n")
            print("Total: {}/{}".format(team.get_score(), team.get_wickets()))

            print("Overs :{}".format(team.over))

            print("Extra: {}".format(team.extra))

            if team.wickets + 1 == number_of_players:
                break

            if team_2.get_score() > team_1.get_score():
                break
            print('')

            index = index + 1  # at last

    print("\n")

    # Result
    if team_1.score > team_2.score:
        print("Result: Team 1 won the match by {} runs.".format(team_1.score - team_2.score))
    elif team_1.score < team_2.score:
        print("Result: Team 2 won the match by {} wickets.".format(number_of_players - team_2.wickets - 1))
    else:
        print("Match Tie")
