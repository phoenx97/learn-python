import character
from sys import exit
from random import randint


class Scene(object):

    def enter(self, player):
        print("This is the default room action. Please specify a room")
        exit(1)


class LobbyRoom(Scene):

    def enter(self, player):
        print("You find yourself in a lobby with a door to the left and right.")
        print("Looks like there is some kind of fire behind the left. The")
        print("right door seems calm. Which door would you like to go through?")

        next_step = raw_input("[left or right]> ")

        if next_step == "left":
            return 'hell_room'

        elif next_step == "right":
            return 'gauntlet_room'

        else:
            return 'game_over'


class HellRoom(Scene):
    def enter(self, player):
        print("You'd really walk into a room already on fire? Welcome to hell!")
        return 'game_over'


class GauntletRoom(Scene):
    
    def enter(self, player):
        print("You walk into the room and see and old man wearing a white\n" +
              "robe, hunched over and leaning on a 6' wooden branch. Good\n" +
              "god, it's Gandalf! And he's about to attack you!")

        gandalf = character.Character('Gandalf', 20)
        bound_keys = player.ability_bind.values()
        player.print_abilities()

        while player.hp > 0 and gandalf.hp > 0:
            action = raw_input("%s> " % sorted(bound_keys))

            if int(action) in bound_keys:
                player.attack(gandalf, int(action))
            else:
                print("Sorry, that is not an acceptable command")

            # random attack! (heal is a little OP in this game)
            gandalf.attack(player, randint(1, len(bound_keys) - 1))

        if player.hp > 0:
            print("You defeated Gandalf! You shall pass after all.")
            return 'victory_room'

        else:
            print("You shall not pass.")
            return 'game_over'


class VictoryRoom(Scene):
    
    def enter(self, player):
        print("You enter a room full of gold and videogames. It's heaven\n" +
              "Congratulations, you win!\n")
        exit(0)


class GameOver(Scene):

    quips = [
        "You died. You kinda suck at this.",
        "Your mom would be proud... if she were smarter.",
        "Such a loser.",
        "I have a small puppy that's better at this."
    ]

    def enter(self, player):
        print(GameOver.quips[randint(0, len(self.quips) - 1)])
        exit(1)


class Map(object):

    scenes = {
        'lobby_room': LobbyRoom(),
        'hell_room': HellRoom(),
        'gauntlet_room': GauntletRoom(),
        'victory_room': VictoryRoom(),
        'game_over': GameOver()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)
