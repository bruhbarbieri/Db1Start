class Greeter:
    def __init__(self, name, formal=False):
        self.name = name
        self.formal = formal

    def greet(self):
        if self.formal:
            print(f"Good morning, {self.name}!")
        else:
            print(f"Hello, {self.name}!")

informal_greeter = Greeter("Pythonista")
informal_greeter.greet()

formal_greeter = Greeter("Pythonista", True)
formal_greeter.greet()