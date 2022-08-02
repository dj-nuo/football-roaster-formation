import random
import json

# all the input variables
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

# forming all players list that are on the field during the switch
roaster = []
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
    # example: 
    #    1  | min 0-10 |  ['Emre', 'Other A', 'Luca', 'Luismi', 'Mohammad', 'Other B', 'Amir', 'Alex', 'Badreddine', 'Muath']
    #    2  | min 10-20 |  ['Luismi', 'Alexander', 'Other A', 'Mohammad', 'Alex', 'Serhii', 'Luca', 'Ahmed Samir', 'Emre', 'Amir']
    #    3  | min 20-30 |  ['Badreddine', 'Luismi', 'Other A', 'Other B', 'Muath', 'Luca', 'Amir', 'Ahmed Samir', 'Alexander', 'Mohammad']
    print(index + 1, f" | min {index * optimal_time_per__switch}-{(index + 1) * optimal_time_per__switch} | ", [player["name"] for player in switch])

# # debug info
print("######################## DEBUG INFO ###############")
for player, switches in switches_per_player.items():
    print(switches, player)
    


