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


class Weapon(Ability):
    """docstring for Weapon."""

    def attack(self):
        damage = random.randint(self.max_damage//2, self.max_damage)
        return damage


class Armor(object):
    """docstring for Armor."""

    def __init__(self, name, max_block):
        super(Armor, self).__init__()
        self.name = name
        self.max_block = max_block

    def block(self):
        block = random.randint(0, self.max_block)
        return block


class Hero(object):
    """docstring for Hero."""

    def __init__(self, name, starting_health=100):
        super(Hero, self).__init__()
        self.name = name
        self.starting_health = starting_health
        self.current_health = self.starting_health
        self.abilities = []
        self.armors = []

    def add_ability(self, ability):
        self.abilities.append(ability)
        pass

    def add_armor(self, armor):
        self.armors.append(armor)
        pass

    def attack(self):
        total_attack = 0
        for ability in self.abilities:
            total_attack += ability.attack()
        return total_attack

    def defend(self, damage_amount):
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        resulting_damage = damage_amount - total_block
        return resulting_damage

    def take_damage(self, damage_amount):
        self.current_health -= self.defend(damage_amount)
        pass

    def is_alive(self):
        if self.current_health <= 0:
            return False
        else:
            return True

    def fight(self, opponent):
        if self.abilities != [] or opponent.abilities != []:
            while self.is_alive() is True and opponent.is_alive() is True:
                opponent.take_damage(self.attack())
                self.take_damage(opponent.attack())
            if self.is_alive() is False and opponent.is_alive() is False:
                print(self.name + " " + opponent.name + " have both died at the same time.")
                pass
            elif self.is_alive is False:
                print(opponent.name + " has won!")
                pass
            else:
                print(self.name + " has won!")
                pass
        else:
            print(self.name + " " + opponent.name + " have tied because they have no abilities")
            pass


class Team(object):
    """docstring for Team."""

    def __init__(self, name):
        self.name = name
        self.heros = {}

    def add_hero(self, hero):
        self.heros[hero.name: hero]
        pass

    def remove_hero(self, hero):
        pass

    def list_heros(self):
        pass



if __name__ == "__main__":
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 50)
    ability2 = Ability("Super Eyes", 50)
    ability3 = Ability("Wizard Wand", 50)
    ability4 = Ability("Wizard Beard", 50)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero2.fight(hero1)
