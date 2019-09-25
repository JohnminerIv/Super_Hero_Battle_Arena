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
        self.kills = 0
        self.deaths = 0

    def add_ability(self, ability):
        self.abilities.append(ability)
        pass

    def add_weapon(self, weapon):
        self.abilities.append(weapon)
        pass

    def add_armor(self, armor):
        self.armors.append(armor)
        pass

    def attack(self):
        total_attack = 0
        for ability in self.abilities:
            total_attack += ability.attack()
        return total_attack

    def defend(self):
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block

    def take_damage(self, damage_amount):
        self.current_health = damage_amount - self.defend()
        pass

    def is_alive(self):
        if self.current_health <= 0:
            return False
        else:
            return True

    def fight(self, opponent):
        if self.abilities != [] and opponent.abilities != []:
            while self.is_alive() is True and opponent.is_alive() is True:
                opponent.take_damage(self.attack())
                self.take_damage(opponent.attack())
            if self.is_alive() is False and opponent.is_alive() is False:
                print(self.name + " " + opponent.name + " have both died at the same time.")
                self.add_kill(1)
                self.add_death(1)
                opponent.add_death(1)
                opponent.add_kill(1)
                pass
            elif self.is_alive is False:
                print(opponent.name + " has won!")
                self.add_death(1)
                opponent.add_kill(1)
                pass
            else:
                print(self.name + " has won!")
                self.add_kill(1)
                opponent.add_death(1)
                pass
        else:
            if self.abilities == []:
                self.current_health = 0
                self.add_death(1)
                opponent.add_kill(1)
                print(f"{self.name} forfits because they have no abilities.")
            elif opponent.abilities == []:
                self.add_kill(1)
                opponent.add_death(1)
                opponent.current_health = 0
                print(f"{opponent.name} forfits because they have no abilities.")
            else:
                self.add_kill(1)
                self.add_death(1)
                opponent.add_death(1)
                opponent.add_kill(1)
                opponent.current_health = 0
                self.current_health = 0
                print(self.name + " " + opponent.name + " have tied because they have no abilities")
            pass

    def add_kill(self, num_kills):
        self.kills += num_kills
        pass

    def add_death(self, num_deaths):
        self.deaths += num_deaths
        pass

    def stats_reset(self):
        self.kills = 0
        self.deaths = 0
        pass


class Team(object):
    """docstring for Team."""

    def __init__(self, name):
        self.name = name
        self.heroes = []

    def add_hero(self, hero):
        self.heroes.append(hero)
        pass

    def remove_hero(self, hero_name):
        list_place = 0
        removed_hero = False
        for hero in self.heroes:
            if hero.name == hero_name:
                self.heroes.pop(list_place)
                removed_hero = True
            list_place += 1
        if removed_hero is False:
            print("I'm sorry I couldn't find that hero in this team.")
            return 0
        pass

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)
        pass

    def attack(self, other_team):
        if self.heroes != [] and other_team.heroes != []:
            for hero in self.heroes:
                if hero.abilities == []:
                    print(f"The hero {hero.name} does not have an ability and will forfit")
            for hero in other_team.heroes:
                if hero.abilities == []:
                    print(f"The hero {hero.name} does not have an ability and will forfit")
            has_alive_heroes = {"team1": True, "team2": True}
            while has_alive_heroes["team1"] is True and has_alive_heroes["team2"] is True:
                heroes_team1 = []
                heroes_team2 = []
                for hero in self.heroes:
                    if hero.is_alive() is True:
                        heroes_team1.append(hero)
                for hero in other_team.heroes:
                    if hero.is_alive() is True:
                        heroes_team2.append(hero)
                len_heroes1 = len(heroes_team1)-1
                print(len_heroes1)
                len_heroes2 = len(heroes_team2)-1
                print(len_heroes2)
                if len_heroes1 == 0 and len_heroes2 == 0:
                    heroes_team1[0].fight(heroes_team2[0])
                elif len_heroes1 > 0 and len_heroes2 == 0:
                    heroes_team1[random.randint(0, len_heroes1)].fight(heroes_team2[0])
                elif len_heroes1 == 0 and len_heroes2 > 0:
                    heroes_team1[0].fight(heroes_team2[random.randint(0, len_heroes2)])
                elif len_heroes1 > 0 and len_heroes2 > 0:
                    heroes_team1[random.randint(0, len_heroes1)].fight(heroes_team2[random.randint(0, len_heroes2)])
                heroes_team1 = []
                heroes_team2 = []
                for hero in self.heroes:
                    if hero.abilities != []:
                        if hero.is_alive() is True:
                            heroes_team1.append(hero)
                for hero in other_team.heroes:
                    if hero.abilities != []:
                        if hero.is_alive() is True:
                            heroes_team2.append(hero)
                if heroes_team1 == []:
                    has_alive_heroes.update({"team1": False})
                if heroes_team2 == []:
                    has_alive_heroes.update({"team2": False})
        else:
            print("One of the teams does not have any heros.")
        pass

    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.current_health = hero.starting_health
        pass

    def stats(self):
        for hero in self.heroes:
            print(f"This hero {hero.name}, killed {hero.kills} hero(es) and died {hero.deaths} time(s).")
        pass

    def reset(self):
        for hero in self.heroes:
            hero.stats_reset()
        pass


class Arena:
    def __init__(self):
        self.team_one = None
        self.team_two = None
        self.weapons = {}
        self.abilities = {}
        self.armors = {}
        self.heroes = {}

    def create_ability(self):
        print("please enter an ability name:")
        name = input()
        while True:
            try:
                print("please tell me how much damage it does")
                damage = int(input())
                break
            except:
                print("That was not an Integer!")

        self.abilities.update({name: Ability(name, damage)})
        print(self.abilities)
        return self.abilities[name]

    def create_weapon(self):
        print("please enter a weapon name:")
        name = input()
        while True:
            try:
                print("please tell me how much damage it does")
                damage = int(input())
                break
            except:
                print("That was not an Integer!")

        self.weapons.update({name: Weapon(name, damage)})
        print(self.weapons)
        return self.weapons[name]

    def create_armor(self):
        print("please enter an armor name:")
        name = input()
        while True:
            try:
                print("please tell me how much damage it can protect from")
                damage = int(input())
                break
            except:
                print("That was not an Integer!")

        self.armors.update({name: Armor(name, damage)})
        print(self.armors)
        return self.armors[name]

    def create_hero(self):
        print("please enter a hero's name:")
        name = input()
        while True:
            try:
                print("""tell me how many hit-points they have. Or D for defualt.""")
                damage = input()
                if damage == "D":
                    damage = 100
                    break
                damage = int(damage)
                break
            except:
                print("That was not an acceptable answer!")

        self.heroes.update({name: Hero(name, damage)})
        print(self.heroes)
        return self.heroes[name]

    def build_team_one(self):
        print("what is team ones name?")
        name = input()
        self.team_one = Team(name)
        while True:
            print("Would you like to edit team one? Y or N")
            user_in = input()
            if user_in == "Y":
                while True:
                    print("""You can add a hero H or quit Q.""")
                    user_in = input()
                    if user_in == "H":
                        hero = self.create_hero()
                        while True:
                            print("""
Would you like to add
abilities 'A', weapons 'W',
armor 'R', or stop customizing hero 'S'?
                            """)
                            user_in = input()
                            if user_in == "W":
                                hero.add_weapon(self.create_weapon())
                            elif user_in == "A":
                                hero.add_ability(self.create_ability())
                            elif user_in == "R":
                                hero.add_armor(self.create_armor())
                            elif user_in == "S":
                                break
                            else:
                                print('Give me proper input!')
                        self.team_one.add_hero(hero)
                    elif user_in == "Q":
                        break
                    else:
                        print("please give me proper input.")
            elif user_in == "N":
                break
            else:
                print("That wasn't an option!")
        pass

    def build_team_two(self):
        print("what is team twos name?")
        name = input()
        self.team_two = Team(name)
        while True:
            print("Would you like to edit team two? Y or N")
            user_in = input()
            if user_in == "Y":
                while True:
                    print("""You can add a hero H or quit Q.""")
                    user_in = input()
                    if user_in == "H":
                        hero = self.create_hero()
                        while True:
                            print("""
Would you like to add
abilities 'A', weapons 'W',
armor 'R', or stop customizing hero 'S'?
                            """)
                            user_in = input()
                            if user_in == "W":
                                hero.add_weapon(self.create_weapon())
                            elif user_in == "A":
                                hero.add_ability(self.create_ability())
                            elif user_in == "R":
                                hero.add_armor(self.create_armor())
                            elif user_in == "S":
                                break
                            else:
                                print('Give me proper input!')
                        self.team_two.add_hero(hero)
                    elif user_in == "Q":
                        break
                    else:
                        print("please give me proper input.")
            elif user_in == "N":
                break
            else:
                print("That wasn't an option!")
        pass

    def team_battle(self):
        self.team_one.attack(self.team_two)
        pass

    def show_statistics(self):
        self.team_one.stats()
        self.team_two.stats()
        while True:
            print("Would you like to reset these stats? Y or N")
            user_in = input()
            if user_in == "Y":
                self.team_one.reset()
                self.team_two.reset()
                break
            elif user_in == "N":
                print("Okay cool")
                break
            else:
                print("That is not an option!")
        pass

    def teams_heal(self):
        self.team_one.revive_heroes()
        self.team_two.revive_heroes()
        print("The combatants have been healed.")



if __name__ == "__main__":
    """
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
    """
    while True:
        ar = Arena()
        while True:
            ar.build_team_one()
            ar.build_team_two()
            while True:
                ar.team_battle()
                ar.show_statistics()
                print("Would you like these two teams to heal and battle again? Y to battle again or any key to edit teams.")
                user_in = input()
                if user_in == "Y":
                    ar.teams_heal()
                    pass
                else:
                    break
            print("Would you like to edit these teams or start over from scratch? Y to edit or any key to reset the Arena.")
            user_in = input()
            if user_in == "Y":
                pass
            else:
                break
        print("Would you like to play again or quit? Y to play again or any key quit.")
        user_in = input()
        if user_in == "Y":
            pass
        else:
            break
