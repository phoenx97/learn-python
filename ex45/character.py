class Character(object):
    # these probably shouldn't be global
    ability_list = ["auto_attack", "magic_attack", "heal"]
    ability_dmg = {"auto_attack": 5, "magic_attack": 8, "heal": 10}
    ability_name = {"auto_attack": "Melee Attack", "magic_attack": "Fireball", "heal": "Esuna"}
    ability_bind = {"auto_attack": 1, "magic_attack": 2, "heal": 3}

    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def debug(self):
        print('%s starts with %d HP' % (self.name, self.hp))
        for ability in self.ability_list:
            print("%r performs %r that does %d damage" % (
                self.ability_bind[ability], self.ability_name[ability],
                self.ability_dmg[ability]))

    def attack(self, opponent, action):
        spell = self.get_ability(action)
        
        if spell == 'heal':
            self.hp += self.ability_dmg[spell]
            print("%s performs %s on %s for %d HP" % (self.name, self.ability_name[spell], self.name, self.ability_dmg[spell]))
        else:
            opponent.hp -= self.ability_dmg[spell]
            print("%s performs %s on %s for %d damage" % (self.name, self.ability_name[spell], opponent.name, self.ability_dmg[spell]))

        print("%s HP: %d, %s HP: %d" % (self.name, self.hp, opponent.name, opponent.hp))

    def get_ability(self, button):
        for key, value in self.ability_bind.items():
            if value == button:
                return key

    def print_abilities(self):
        abilities = 'Your abilities: '
        for bind in sorted(self.ability_bind, key=self.ability_bind.get):
            abilities += "%d. %s " % (self.ability_bind[bind], self.ability_name[bind])
        print(abilities)
