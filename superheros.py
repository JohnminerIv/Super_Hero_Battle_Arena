import random
""" Ability Class
__init__: Parameters: name: String, max_damage: Integer
attack: No Parameters
Armor Class
__init__: Parameters: name: String, max_block: Integer
block: Parameters: None
Hero Class
__init__: Parameters: name:String, starting_health:Int (default value: 100)
add_ability: Parameters: ability:Ability Object
attack: No Parameters
defend: incoming_damage: Integer
take_damage: Parameters: damage
is_alive: No Parameters
fight: Parameters: opponent: Hero Class """


class Ability(object):
    """docstring for Ability."""

    def __init__(self, name, max_damage):
        super(Ability, self).__init__()
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        damage = random.randint(0, self.max_damage)
        return damage


class Armor(object):
    """docstring for Armor."""

    def __init__(self, arg):
        super(Armor, self).__init__()
        self.arg = arg


class Hero(object):
    """docstring for Hero."""

    def __init__(self, arg):
        super(Hero, self).__init__()
        self.arg = arg


debugging = Ability("Debgguing", 7)
print(debugging.name)
print(debugging.attack())
