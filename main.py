import random
import json

roaster = []

total_time_min = 120
number_of_teams = 2
max_players_per_team = 5
total_players_on_the_field = number_of_teams * max_players_per_team
players = json.load(open("players.json"))
number_of_players = print(len(players))

# dict for final debugging
# example: {'Alex': 0, 'Emre': 0, 'Mohammad': 0, ...}
switches_per_player = {name["name"]:0 for name in players}

# need to calculate optimal time per switch, so that everybody plays ~ the same amount of time
optimal_time_per__switch = 10
total_switches = int(total_time_min / optimal_time_per__switch)

for switch in range(total_switches):
    random.shuffle(players)
    roaster.append(players[0:total_players_on_the_field])

# print(roaster)

# calculating amount of games that each player plays "de facto"
# and generating roaster info for the user
for index, switch in enumerate(roaster):
    for player in switch:
        switches_per_player[player["name"]] += 1
    
    # outputting every switch
    print(index + 1, f" | min {index * optimal_time_per__switch}-{(index + 1) * optimal_time_per__switch} | ",switch)

# # debug info
print("######################## DEBUG INFO ###############")
for player, switches in switches_per_player.items():
    print(switches, player)
    


