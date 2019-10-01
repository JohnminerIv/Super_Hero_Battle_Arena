class Animal(object):
    """docstring for Animal."""

    def __init__(self, name, sleep_time):
        super(Animal, self).__init__()
        self.name = name
        self.sleep_time = sleep_time

    def eat(self, food):
        print(f"{self.name} ate the {food}!")

    def drink(self):
        print(f"{self.name} drank some water!")

    def sleep(self):
        print(f"{self.name} selpt for {self.sleeptime} hours!")
