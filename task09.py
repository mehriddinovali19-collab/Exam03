class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    
    def make_sound(self):
        print(f'{self.name} says {self.sound}')

anim = Animal("dog", "woof")
anim2 = Animal("cow", "Mu")
anim.make_sound()
anim2.make_sound()