import character, engine, maps

print("Welcome to the game! Please enter your name")
player_name = raw_input("> ")
player = character.Character(player_name, 100)
print("Welcome %s. You start the game with %d HP" % (player.name, player.hp))
game_map = maps.Map('lobby_room')
game_engine = engine.Engine(game_map, player)
game_engine.play()