from nose.tools import *
from ex45.character import Character


def test_character():
    player = Character('Player', 100)
    assert_equal(player.name, 'Player')
    assert_equal(player.hp, 100)

def test_abilities():
    ability_list = ["auto_attack", "magic_attack", "heal"]
    ability_dmg = {"auto_attack": 5, "magic_attack": 8, "heal": 10}
    ability_name = {"auto_attack": "Melee Attack", "magic_attack": "Fireball", "heal": "Esuna"}
    ability_bind = {"auto_attack": 1, "magic_attack": 2, "heal": 3}
    assert_equal(Character.ability_list, ability_list)
    assert_equal(Character.ability_dmg, ability_dmg)
    assert_equal(Character.ability_name, ability_name)
    assert_equal(Character.ability_bind, ability_bind)

def test_attack():
    player = Character('Player', 100)
    opponent = Character('Enemy', 100)
    player.attack(opponent, 1)
    assert_equal(opponent.hp, 95)
    player.attack(opponent, 2)
    assert_equal(opponent.hp, 87)
    player.attack(player, 3)
    assert_equal(player.hp, 110)
