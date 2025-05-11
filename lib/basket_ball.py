def game_dict():
    return {
        "home": {
            "team_name": "Cleveland Cavaliers",
            "colors": ["Wine", "Gold"],
            "players": [
                {
                    "name": "Jarrett Allen",
                    "number": 31,
                    "position": "Center",
                    "points_per_game": 16.1,
                    "rebounds_per_game": 10.8,
                    "assists_per_game": 1.6,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.3,
                    "career_points": 3945,
                    "age": 24,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Darius Garland",
                    "number": 10,
                    "position": "Point Guard",
                    "points_per_game": 21.7,
                    "rebounds_per_game": 3.3,
                    "assists_per_game": 8.6,
                    "steals_per_game": 1.3,
                    "blocks_per_game": 0.1,
                    "career_points": 3142,
                    "age": 22,
                    "height_inches": 73,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Evan Mobley",
                    "number": 4,
                    "position": "Center",
                    "points_per_game": 15.0,
                    "rebounds_per_game": 8.3,
                    "assists_per_game": 2.5,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.7,
                    "career_points": 1034,
                    "age": 21,
                    "height_inches": 83,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Kevin Love",
                    "number": 0,
                    "position": "Power Forward",
                    "points_per_game": 13.6,
                    "rebounds_per_game": 7.2,
                    "assists_per_game": 2.2,
                    "steals_per_game": 0.4,
                    "blocks_per_game": 0.2,
                    "career_points": 14305,
                    "age": 34,
                    "height_inches": 80,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Isaac Okoro",
                    "number": 35,
                    "position": "Small Forward",
                    "points_per_game": 8.8,
                    "rebounds_per_game": 3.0,
                    "assists_per_game": 1.8,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 0.3,
                    "career_points": 1234,
                    "age": 21,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Ricky Rubio",
                    "number": 99,
                    "position": "Point Guard",
                    "points_per_game": 13.1,
                    "rebounds_per_game": 4.1,
                    "assists_per_game": 6.6,
                    "steals_per_game": 1.4,
                    "blocks_per_game": 0.2,
                    "career_points": 7399,
                    "age": 31,
                    "height_inches": 74,
                    "shoe_brand": "Adidas",
                },
            ],
        },
            
        "away": {
            "team_name": "Washington Wizards",
            "colors": ["Red", "White", "Navy Blue"],
            "players": [   
                {
                    "name": "Bradley Beal",
                    "number": 3,
                    "position": "Shooting Guard",
                    "points_per_game": 23.2,
                    "rebounds_per_game": 4.7,
                    "assists_per_game": 6.6,
                    "steals_per_game": 0.9,
                    "blocks_per_game": 0.4,
                    "career_points": 14231,
                    "age": 29,
                    "height_inches": 76,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kyle Kuzma",
                    "number": 33,
                    "position": "Power Forward",
                    "points_per_game": 17.1,
                    "rebounds_per_game": 8.5,
                    "assists_per_game": 3.5,
                    "steals_per_game": 0.6,
                    "blocks_per_game": 0.9,
                    "career_points": 5336,
                    "age": 27,
                    "height_inches": 81,
                    "shoe_brand": "Puma",
                },
                {
                    "name": "Kentavious Caldwell-Pope",
                    "number": 1,
                    "position": "Shooting Guard",
                    "points_per_game": 13.2,
                    "rebounds_per_game": 3.4,
                    "assists_per_game": 1.9,
                    "steals_per_game": 1.1,
                    "blocks_per_game": 0.3,
                    "career_points": 7911,
                    "age": 29,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Davis Bertans",
                    "number": 42,
                    "position": "Power Forward",
                    "points_per_game": 5.6,
                    "rebounds_per_game": 2.1,
                    "assists_per_game": 0.6,
                    "steals_per_game": 0.3,
                    "blocks_per_game": 0.3,
                    "career_points": 3165,
                    "age": 29,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kristaps Porzingis",
                    "number": 6,
                    "position": "Power Forward",
                    "points_per_game": 22.1,
                    "rebounds_per_game": 8.8,
                    "assists_per_game": 2.9,
                    "steals_per_game": 0.7,
                    "blocks_per_game": 1.5,
                    "career_points": 6371,
                    "age": 27,
                    "height_inches": 87,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Rui Hachimura",
                    "number": 8,
                    "position": "Power Forward",
                    "points_per_game": 11.3,
                    "rebounds_per_game": 3.8,
                    "assists_per_game": 1.1,
                    "steals_per_game": 0.5,
                    "blocks_per_game": 0.2,
                    "career_points": 1913,
                    "age": 24,
                    "height_inches": 80,
                    "shoe_brand": "Jordan",
                },
            ]
        }
    }

#Code starting here
match = game_dict() #storing game data in match (global var to access in all functions below)

# Geting Name of player to use across the functions
def get_player (name_of_player):
    for team in match.values():
        for player in team["players"]:
            if player["name"] == name_of_player:
                return player
    return "Did NOt get PLayer"

print(get_player ("Jarrett Allen"))

# Geting Team Name of playerr to use across the functions 
def get_team (name_of_team):
    for team in match.values():
        if team["team_name"] == name_of_team:
            return team

print(get_team ("Cleveland Cavaliers"))

# num_points_per_game()
def num_points_per_game(name_of_player) :
    player = get_player(name_of_player)
    if player:
        return player["points_per_game"]
    return "No points for game found"

print(num_points_per_game ("Jarrett Allen"))

# player_age()
def player_age(name_of_player):
    player = get_player(name_of_player)
    if player:
        return player["age"]
    return "Couldnt Find Age"

print(player_age("Jarrett Allen"))

# team_colors()
def team_colors(name_of_team):
    team = get_team (name_of_team)
    if team:
        return team["colors"]
    return "Team Colors Not Found"
    
print(team_colors("Cleveland Cavaliers"))

# team_names()
def team_names():
    return [team["team_name"] for team in match.values()]


print (team_names())

# player_numbers()
def player_numbers(name_of_team):
    team = get_team (name_of_team)
    if team:
        numbers = []
        for player in team["players"]:
            numbers.append(player["number"])
        return numbers
    return "NUmbers not found"
                
print (player_numbers("Cleveland Cavaliers"))

# player_stats()
def player_stats(name_of_player):
    player = get_player(name_of_player)
    if player:
        return player
    return "Player Stats Unavailable"

print(player_stats("Jarrett Allen"))

# average_rebounds_by_shoe_brand()   (Nike-7,Adidas-3,Puma-1,Jordan-1)

def average_rebounds_by_shoe_brand(name_of_player):
    nike = []
    adidas = []
    puma = []
    jordan = []

    player = get_player(name_of_player)
    if player:
        brand = player["shoe_brand"]
        rebounds = player["rebounds_per_game"]

        if brand == "Nike":
            nike.append(rebounds)
            average_rebounds = sum(nike) / len(nike)
            print(f"{brand}: {average_rebounds:.2f}")
        
        elif brand == "Adidas":
            adidas.append(rebounds)
            average_rebounds = sum(adidas) / len(adidas)
            print(f"{brand}: {average_rebounds:.2f}")
        
        elif brand == "Puma":
            puma.append(rebounds)
            average_rebounds = sum(puma) / len(puma)
            print(f"{brand}: {average_rebounds:.2f}")
        
        elif brand == "Jordan":
            jordan.append(rebounds)
            average_rebounds = sum(jordan) / len(jordan)
            print(f"{brand}: {average_rebounds:.2f}")
        
        return average_rebounds
    else:
        return "Player Not Found"


print(average_rebounds_by_shoe_brand("Jarrett Allen"))
