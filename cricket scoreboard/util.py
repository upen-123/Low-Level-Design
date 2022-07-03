def swap(object_1, object_2):
    return object_2, object_1


def process_a_over(team, strike_player, non_strike_player, player_number, balls_in_a_over, number_of_players, team_1,
                   team_2, bowler):
    while balls_in_a_over > 0:
        item = input()
        if item not in ["W", "Nb", "Wd", "1", "2", "3", "4", "6", "0"]:
            print("Please Enter a valid input.")
            continue

        if item == 'Wd' or item == 'Nb':
            team.extra += 1
            bowler.extra += 1

        elif item == 'W':
            balls_in_a_over -= 1
            strike_player.balls += 1
            strike_player.not_out, strike_player.currently_playing = False, False
            team.wickets += 1
            bowler.wickets += 1
            if team.wickets + 1 == number_of_players:  # when all the wickets fall
                break
            strike_player = team.batting_order[player_number]
            strike_player.currently_playing = True
            player_number += 1
        else:
            balls_in_a_over -= 1
            strike_player.balls += 1
            strike_player.score += int(item)
            bowler.run_concede += int(item)

            if item == '1' or item == '3':
                # swapping strike
                strike_player, non_strike_player = swap(strike_player, non_strike_player)
            elif item == '4':
                strike_player.fours += 1
            elif item == '6':
                strike_player.sixes += 1
            else:
                pass

        # When Team 2 win the match
        if team_2.get_score() > team_1.get_score():
            break

        if balls_in_a_over == 0:
            # swapping striker and non-striker at last ball of the over
            strike_player, non_strike_player = swap(strike_player, non_strike_player)
    return balls_in_a_over
