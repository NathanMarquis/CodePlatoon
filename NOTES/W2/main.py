class Dog: #capital letters for titles
    #dunder-init (double underscores) is a dunder method mainly to define classes
    def __init__(self, name, color, sound): #self refers to dog object we're about to make
        self.name = name
        self.species = 'Dog'
        self.color = color
        self.sound = sound
        #print('initialising!')
    def __str__(self):
        return f"I am a {self.color} {self.species} named {self.name}."
    def speak(self):
        print(f">> {self.sound}!")
    def fetch(self, item):
        print(f"{self.name} fetched the {item}!")
fido = Dog('Fido', 'brown', 'woof') #callable like functions in python
print(fido)
fido.speak()
fido.fetch('bone')

# print(Dog)
# print(fido.name)