from nose.tools import *
from ex45.maps import *
from ex45.character import Character

def test_lobby():
    lobby = LobbyRoom()
    player = Character('Player', 100)
    # get input from maps_inputs.txt
    assert lobby.enter(player) == 'game_over'
    assert lobby.enter(player) == 'hell_room'
    assert lobby.enter(player) == 'gauntlet_room'

def test_hell():
    room = HellRoom()
    player = Character('Player', 100)
    assert room.enter(player) == 'game_over'

def test_gauntlet():
    room = GauntletRoom()
    player = Character('Player', 100)
    assert room.enter(player) == 'victory_room'
    
    room2 = GauntletRoom()
    player2 = Character('Player', 1)
    assert room2.enter(player2) == 'game_over'

def test_map():
    game_map = Map('lobby_room')
    assert_equal(game_map.start_scene, 'lobby_room')
