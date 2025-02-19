class Greeter:
    def __init__(self, message):
        self.message = message

    def greet(self):
        print(self.message)

g = Greeter("Hello, World!")
g.greet()
