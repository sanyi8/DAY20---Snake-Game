class Animal:
    def __init__(self):
        self.num_eyes = 2
    def breathe(self):
        print("Inhale, exhale.")

class Fish:
    def swim(self):
        print("moving in water.")


nemo = Fish()
nemo.swim()