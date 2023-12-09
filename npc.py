class NPC:
    def __init__(self, name, race, age, wearing, wielding):
        self.name = name
        self.race = race
        self.age = age
        self.wearing = wearing
        self.wielding = wielding
    def __str__(self):
        return f"NPC - Name: {self.name}, Race: {self.race}, Age: {self.age}, Wearing: {self.wearing}, Wielding: {self.wielding}"
    def save_to_file(self):
        with open(f"{self.name}.txt", "w") as file:
            file.write(str(self))
