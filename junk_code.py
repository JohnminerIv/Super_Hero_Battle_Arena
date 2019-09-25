def create_hero(self, team):
    print("What is the heroes name?")
    name = input()
    while True:
        print("would you like to set a starting health? The default is 100. Y or N")
        default_health = input()
        if default_health == "Y":
            while True:
                try:
                    print("what is the heroes starting health?")
                    default_health = int(input())
                    break
                except ValueError:
                    print("That does not seem to be a number try again.")
        elif default_health == "N":
            default_health = 100
            break
        else:
            print("You didn't enter an option.")
    if team == 1:
        location_in_list = len(self.heroes)
        self.heroes[location_in_list] = Hero(name, default_health)
        self.team_one.append(self.heroes[location_in_list])
    elif team == 2:
        location_in_list = len(self.heroes)
        self.heroes[location_in_list] = Hero(name, default_health)
        self.team_two.append(self.heroes[location_in_list])
    while True:
        print("Would you like to create another hero?")
        new_hero = input()
        if new_hero == "Y":
            self.create_hero(team)
        elif new_hero == "N":
            while True:
                pass

def build_team_one(self):
    while True:
        print("Enter a name for team one.")
        name = input()
        self.team_one = Team(name)
        print("Would you like to add a hero to team one? Y or N")
        choice = input()
        if choice == "Y":
            self.create_hero(1)
        elif choice == "N":
