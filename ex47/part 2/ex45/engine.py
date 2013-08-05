import maps


class Engine(object):

    def __init__(self, game_map, player):
        self.game_map = game_map
        self.player = player

    def play(self):
        current_scene = self.game_map.opening_scene()

        while True:
            print("\n----------")
            next_scene_name = current_scene.enter(self.player)
            current_scene = self.game_map.next_scene(next_scene_name)
