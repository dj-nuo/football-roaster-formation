from roaster import *

roaster = Roaster(players_json_file="players.json", min_time_per_switch=1, max_time_per_switch=10)

roaster.calculate_optimal_time_per_switch()

# roaster.optimal_time_per_switch = 7
# roaster.generate_roaster()
roaster.calculate_switches_per_player(print_output=True)
roaster.print_roaster()
roaster.generate_players_matrix()
