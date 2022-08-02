from roaster import *

roaster = Roaster(players_json_file="players.json")

switch = print(roaster.generate_random_switch())
roaster.generate_roaster()
roaster.calculate_switches_per_player(print_output=True)
# roaster.generate_players_matrix()
