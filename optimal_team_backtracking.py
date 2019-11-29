class Team:
    def __init__(self, team_list=None):
        """
        Construct the data held by the Team object:

        self.team_list: A list of players in the team, each given as a player dictionary with the structure
            player = {
                'ID': <player name> + " ",
                'position': <forward, centre, back or ruck>,
                'price': <integer price in $>,
                'projScore': <float projected score>
            }
        self.positions: A dictionary with keys 'forward', 'centre', 'back', 'ruck'.
            Each holds a list of players in the team that belong to that position.
        self.salaries: total price of all the players on the team.
        self.scores: total projected scores of all the players on the team.

        :param team_list: A list of correctly-formatted player dictionaries. Can be used to initialise the team.
        """
        self.team_list = team_list if team_list is not None else []
        self.positions = {
            'forward': [],
            'centre': [],
            'back': [],
            'ruck': []
        }

        salaries = 0
        scores = 0
        for player in self.team_list:
            salaries += player['price']
            scores += player['projScore']
        self.salaries = salaries
        self.scores = scores

        self.__initialise_positions()

    def __str__(self):
        name_string = "".join([player['ID'] for player in self.team_list])
        return str(round(self.scores, 2)) + "; " + name_string

    def __initialise_positions(self):
        """Called by the constructor. Populates self.positions with data from self.team_list"""
        for player in self.team_list:
            player_position = player['position']
            self.positions[player_position].append(player)

    def initialise_from_team_list(self, team_list):
        """
        Reconstruct the team from a new team_list

        :param team_list: A list of correctly-formatted player dictionaries.
        """
        self.__init__(team_list)

    def push_player(self, player):
        """
        Add a player to the team.

        Update self.team_list, self.positions,self.salaries and self.scores accordingly.
        :param player: A player dictionary, with the structure
            player = {
                'ID': <player name> + " ",
                'position': <forward, centre, back or ruck>,
                'price': <integer price in $>,
                'projScore': <float projected score>
            }
        """
        # Add ew player to the team
        self.team_list.append(player)

        # Add player to their position
        player_position = player['position']
        self.positions[player_position].append(player)

        # Adjust total salaries and scores
        self.salaries += player['price']
        self.scores += player['projScore']

    def pop_player(self):
        """
        Remove the last-added player from the team.

        Update self.team_list, self.positions,self.salaries and self.scores accordingly.
        :return: The player removed from the team. Returned as a player dictionary, with the structure
            player = {
                'ID': <player name> + " ",
                'position': <forward, centre, back or ruck>,
                'price': <integer price in $>,
                'projScore': <float projected score>
            }
        """
        # Pop last player from the team
        player = self.team_list.pop()

        # Remove popped player from their position
        player_position = player['position']
        self.positions[player_position].pop()

        # Adjust total salaries and scores
        self.salaries -= player['price']
        self.scores -= player['projScore']

        return player


def get_best_team(players, budget):
    """
    Find the team with the highest projected score, whose total salaries are less than the budget.

    The team is comprised of 2 forwards, 4 centres, 2 backs and 1 ruck player.

    :precondition: The Team class must be defined, with attributes self.team_list, self.scores, self.salaries
        and methods self.push_player(), self.pop_player and self.initialise_from_team_list().
    :param players: A tuple with structure (forwards, centres, backs, rucks) where each element is a list containing
        all available players of the corresponding position, where each player is a dictionary with the structure
        player = {
                'ID': <player name> + " ",
                'position': <forward, centre, back or ruck>,
                'price': <integer price in $>,
                'projScore': <float projected score>
            }
    :param budget: An integer total salary for the team, in $.
    :return: The team with the highest projected score
    """

    # These act as global variables within the scope of get_best_team().
    PLAYERS = players
    BUDGET = budget

    def get_next_possible_players(partial_team):
        """
        Generate a list of possible players to add to the team, given the current partial_team.

        :precondition: A list of all available players, PLAYERS, must be defined in the outer scope.
        :precondition: An integer value, BUDGET, must be defined in the outer scope.
        :param partial_team: A Team object
        :return: A list of possible players to add to the team
        """
        next_players_list = []

        # Limit the next possible players based on the positions filled in the team
        if len(partial_team.team_list) < 2:  # 2 forwards
            possible_players = PLAYERS[0]
        elif len(partial_team.team_list) < 6:  # 4 centres
            possible_players = PLAYERS[1]
        elif len(partial_team.team_list) < 8:  # 2 backs
            possible_players = PLAYERS[2]
        elif len(partial_team.team_list) < 9:  # 1 ruck
            possible_players = PLAYERS[3]
        else:
            return next_players_list  # Return the empty list. The team is full, and no players can be added

        for idx, player in enumerate(possible_players):
            # Include only players that do not exceed the total team budget
            if player['price'] + partial_team.salaries <= BUDGET:
                if len(partial_team.team_list) in (0, 2, 6, 8):
                    # Add a player in a new position
                    next_players_list.append(player)
                else:
                    # Add a player in a partially-filled position
                    last_index = possible_players.index(partial_team.team_list[-1])
                    if idx > last_index:
                        # Add only if the new player appears in possible_players later than the last player.
                        # This avoids different permutations of the same combination of players,
                        # and avoids repetitions of the same player.
                        next_players_list.append(player)

        return next_players_list

    def best_team_backtracking(partial_team, current_best_team):
        """
        Implement a backtracking algorithm to find the best team

        :param partial_team: The current partial solution. A Team object.
        :param current_best_team: The solution with the highest total projected score found so far. A Team object
        :postconidition: Modify partial_team and current_best_team in place. Both must be assigned to variables before
            the function call. Then, after the function terminates, current_best_team will contain the solution.
        """
        next_players_list = get_next_possible_players(partial_team)
        # Base case. The team is full.
        if len(next_players_list) == 0:
            # Check if the projected score extends the maximum so far. Replace current_best_team if it does.
            if partial_team.scores > current_best_team.scores:
                assert partial_team.salaries <= BUDGET  # Is accounted for in get_next_possible_players().
                current_best_team.initialise_from_team_list(partial_team.team_list[:])  # Modify in place
                print("\t" + str(current_best_team))

        # Recursive case. Try adding each possible player in turn.
        else:
            for next_player in next_players_list:
                # Print when the first player changes to track progress.
                if len(partial_team.team_list) == 0:
                    print("with " + str(next_player['ID']) + ":")
                # Recurse with the new player in the team
                partial_team.push_player(next_player)
                best_team_backtracking(partial_team, current_best_team)
                partial_team.pop_player()

    partial_team = Team()
    solution = Team()
    best_team_backtracking(partial_team, solution)
    return solution


if __name__ == '__main__':
    # Construct player data
    forwardDetails = [
        {'ID': "Degoey ", 'position': "forward", 'price': 10980, 'projScore': 99},
        {'ID': "Christensen ", 'position': "forward", 'price': 10680, 'projScore': 74},
        {'ID': "McStay ", 'position': "forward", 'price': 7190, 'projScore': 51.33},
        {'ID': "McCarthy ", 'position': "forward", 'price': 8250, 'projScore': 63.33},
        {'ID': "Cameron ", 'position': "forward", 'price': 9370, 'projScore': 58.33},
        {'ID': "Hipwood ", 'position': "forward", 'price': 8040, 'projScore': 64},
        {'ID': "Varcoe ", 'position': "forward", 'price': 8010, 'projScore': 52.67},
        {'ID': "Mathieson ", 'position': "forward", 'price': 8530, 'projScore': 57.67},
        {'ID': "McInerney ", 'position': "forward", 'price': 7850, 'projScore': 64.67},
        {'ID': "Elliott ", 'position': "forward", 'price': 8310, 'projScore': 48.33},
        {'ID': "Thomas ", 'position': "forward", 'price': 8700, 'projScore': 62.33},
        {'ID': "Rayner ", 'position': "forward", 'price': 8240, 'projScore': 43},
        {'ID': "Stephenson ", 'position': "forward", 'price': 9770, 'projScore': 74.67}
    ]
    centreDetails = [
        {'ID': "Lyons ", 'position': "centre", 'price': 12150, 'projScore': 69.67},
        {'ID': "Adams ", 'position': "centre", 'price': 15740, 'projScore': 99},
        {'ID': "Pendlebury ", 'position': "centre", 'price': 13060, 'projScore': 89.33},
        {'ID': "Sidebottom ", 'position': "centre", 'price': 14260, 'projScore': 97.67},
        {'ID': "Treloar ", 'position': "centre", 'price': 15340, 'projScore': 110.67},
        {'ID': "Neale ", 'position': "centre", 'price': 16220, 'projScore': 140},
        {'ID': "Robinson ", 'position': "centre", 'price': 12250, 'projScore': 92.33},
        {'ID': "Zorko ", 'position': "centre", 'price': 13410, 'projScore': 89.67},
        {'ID': "Phillips ", 'position': "centre", 'price': 13300, 'projScore': 99},
        {'ID': "Beams ", 'position': "centre", 'price': 15830, 'projScore': 101.33},
        {'ID': "Berry ", 'position': "centre", 'price': 12460, 'projScore': 91},
        {'ID': "McCluggage ", 'position': "centre", 'price': 11970, 'projScore': 79.67},
        {'ID': "Brown ", 'position': "centre", 'price': 8200, 'projScore': 53}
    ]
    backDetails = [
        {'ID': "Crisp ", 'position': "back", 'price': 12590, 'projScore': 85.33},
        {'ID': "Langdon ", 'position': "back", 'price': 9980, 'projScore': 71.67},
        {'ID': "Maynard ", 'position': "back", 'price': 10080, 'projScore': 83},
        {'ID': "Moore ", 'position': "back", 'price': 8110, 'projScore': 63.33},
        {'ID': "Andrews ", 'position': "back", 'price': 10100, 'projScore': 63.67},
        {'ID': "Gardiner ", 'position': "back", 'price': 9350, 'projScore': 51},
        {'ID': "Rich ", 'position': "back", 'price': 11190, 'projScore': 91.67},
        {'ID': "Robertson ", 'position': "back", 'price': 9210, 'projScore': 53},
        {'ID': "Walker ", 'position': "back", 'price': 10660, 'projScore': 80.33},
        {'ID': "Hodge ", 'position': "back", 'price': 9760, 'projScore': 63.67},
        {'ID': "Aish ", 'position': "back", 'price': 10020, 'projScore': 72},
        {'ID': "Howe ", 'position': "back", 'price': 10440, 'projScore': 81},
        {'ID': "Witherden ", 'position': "back", 'price': 13850, 'projScore': 90.33},
        {'ID': "Mihocek ", 'position': "back", 'price': 9980, 'projScore': 80.67}
    ]
    ruckDetails = [
        {'ID': "Grundy ", 'position': "ruck", 'price': 16770, 'projScore': 129},
        {'ID': "Roughead ", 'position': "ruck", 'price': 9050, 'projScore': 67.33},
        {'ID': "Martin ", 'position': "ruck", 'price': 12450, 'projScore': 81.67},
        {'ID': "Cox ", 'position': "ruck", 'price': 8530, 'projScore': 59.67}
    ]

    player_details = (forwardDetails, centreDetails, backDetails, ruckDetails)

    # Find and display best team
    best_team = get_best_team(player_details, 100000)
    print()
    print("best projected score; best team:")
    print(best_team)
