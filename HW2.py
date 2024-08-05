games = ["Auto Theft Grand V", "Fortnite", "The Elder Scrolls V: Skyrim", "Dark Souls", "Overwatch"]

long_name_games = list(filter(lambda game: len(game.replace(" ", "")) > 8, games))

print("Games with names longer than 8 letters are:")
print(long_name_games)


games_starting_with_F = list(filter(lambda game: game.startswith('F'), games))

print("Games with names starring with the letter 'F' are:")
print(games_starting_with_F)

games_names_with_two_word = list(filter(lambda game: len(game.split()) == 2, games))

print("Games with two word only ")
print(games_names_with_two_word)

games_with_V_in_there_names = list(filter(lambda game: 'V' in game, games))
print("Games with V in the names are")
print(games_with_V_in_there_names)

