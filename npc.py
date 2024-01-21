class NPC:
    def __init__(self, name, race, age, wearing, wielding, background):
        self.name = name
        self.race = race
        self.age = age
        self.wearing = wearing
        self.wielding = wielding
        self.background = background
    def __str__(self):
        return f"NPC - Name: {self.name}, Race: {self.race}, Age: {self.age}, Wearing: {self.wearing}, Wielding: {self.wielding}, Background: {self.background}"
    def save_to_file(self):
        with open(f"{self.name}.txt", "w") as file:
            file.write(str(self))
