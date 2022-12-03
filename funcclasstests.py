class Person:

    def __init__(self, name, function):
        self.name = name
        self.function = function

    def play(self):
        print("PLAY")

    def run(self):
        print("RUNNING!")

    def walk(self):
        print("WALKING!!!")

def play():
    print('play')

Joe = Person("Joe", play)

Joe.function()
