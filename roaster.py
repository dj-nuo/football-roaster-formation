import json
import random
import copy
import pandas as pd
import time

# currently supports only 2 teams


class Roaster:
    def __init__(self, players_json_file, total_time_min=120, max_players_per_team=5, min_time_per_switch=5, max_time_per_switch=10):
        self.players = json.load(open(players_json_file))
        self.player_names = [name["name"] for name in self.players]
        self.number_of_players = len(self.players)
        self.total_time_min = total_time_min
        # for now only consider 2 teams, and don't design application for other cases
        self.number_of_teams = 2
        self.max_players_per_team = max_players_per_team
        self.total_players_on_the_field = self.number_of_teams * self.max_players_per_team

        if self.number_of_players < self.total_players_on_the_field:
            raise Exception(
                "Number of players cannot be less than total planned players on the field")

        self.min_time_per_switch = min_time_per_switch
        self.max_time_per_switch = max_time_per_switch

    def calculate_optimal_time_per_switch(self):
        for time_per_switch in range(self.min_time_per_switch, self.max_time_per_switch + 1):
            self.optimal_time_per_switch = time_per_switch
            self.total_switches = int(
                self.total_time_min / self.optimal_time_per_switch)
            self.generate_roaster(print_output=False)

            switches_per_player_deviation = self.calculate_switches_per_player_deviation()
            if switches_per_player_deviation == 0:
                print(self.optimal_time_per_switch,
                      " minutes per switch. First found perfect result selected.")
                return self.optimal_time_per_switch
        print(time_per_switch, " minutes per switch. No perfect result found.")
        return self.optimal_time_per_switch

    def generate_random_switch(self):
        random.shuffle(self.players)
        return self.players[0:self.total_players_on_the_field]

    def generate_roaster(self, print_output=True):
        self.roaster = []
        for switch in range(self.total_switches):
            # keep brute forcing until balanced next switch is not found (where nobody is left out for more than 1 game)
            while True:
                self.roaster.append(self.generate_random_switch())
                if self.calculate_switches_per_player_deviation() >= 2:
                    self.roaster.pop()
                else:
                    break

        return self.roaster

    def print_roaster(self):
        # calculating amount of games that each player plays "de facto"
        # and generating roaster info for the user
        for index, switch in enumerate(self.roaster):
            # outputting every switch
            # example:
            #    1  | min 0-10 |  ['Emre', 'Other A', 'Luca', 'Luismi', 'Mohammad', 'Other B', 'Amir', 'Alex', 'Badreddine', 'Muath']
            #    2  | min 10-20 |  ['Luismi', 'Alexander', 'Other A', 'Mohammad', 'Alex', 'Serhii', 'Luca', 'Ahmed Samir', 'Emre', 'Amir']
            #    3  | min 20-30 |  ['Badreddine', 'Luismi', 'Other A', 'Other B', 'Muath', 'Luca', 'Amir', 'Ahmed Samir', 'Alexander', 'Mohammad']
            print(index + 1,
                  f" | min {index * self.optimal_time_per_switch}-{(index + 1) * self.optimal_time_per_switch} | ",
                  [player["name"] for player in switch])

    def calculate_switches_per_player(self, print_output=True):
        # example: {'Alex': 0, 'Emre': 0, 'Mohammad': 0, ...}
        switches_per_player = {name["name"]: 0 for name in self.players}
        for index, switch in enumerate(self.roaster):
            for player in switch:
                switches_per_player[player["name"]] += 1

        if print_output:
            print("######################## DEBUG INFO ###############")
            for player, switches in switches_per_player.items():
                print(switches, player)

        return switches_per_player

    def calculate_switches_per_player_deviation(self):
        switches_per_player = self.calculate_switches_per_player(
            print_output=False)
        all_numbers = []
        for player, switches in switches_per_player.items():
            all_numbers.append(switches)

        deviation = max(all_numbers) - min(all_numbers)
        return deviation

    def generate_players_matrix(self):
        # Matrix player vs player
        # How many switches one player played with other on the field
        # TODO in the same team
        # Importing Pandas to create DataFrame
        print("\n################## \nMatrix player vs player")

        # Creating DataFrame and Storing it in variable df

        df = pd.DataFrame(data=0,
                          index=self.player_names,
                          columns=self.player_names
                          )

        for switch in self.roaster:
            for player_a in switch:
                player_a = player_a["name"]
                for player_b in switch:
                    player_b = player_b["name"]
                    if player_a != player_b:
                        df.at[player_a, player_b] += 1
                    else:
                        df.at[player_a, player_b] = 10000

        # Printing DataFrame
        print(df)
