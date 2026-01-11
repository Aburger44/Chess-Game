# just want to try my hand at object orieinted code first before going full functional
class person:
    def __init__(self, name, age, height, weight, mood):
        self.name = name
        self.age = age
        self.height = height
        self.wight = weight
        self.mood = mood
    def says(self):
        print(f"{self.name} says hello!")
    human = True
person1 = person("Alice", 30, "5'6\"", 130, "happy")
# all of the atributes in init function are required
person2 = person("Bob", 25, "5'8\"", 150, "neutral")
person2.age += 1  # Bob has a birthday
print(person2.age)  # Output: 26
person1.ugly = True  # Adding a new attribute 'ugly' to person1
print(f"He is ugly? {person1.ugly}")  # Output: True
person2.human = False  # Changing the class attribute 'human' for person2
print(f"Is Bob human? {person2.human}")  # Output: False
person1.says()  # Output: Alice says hello!