class Bird:
    def __init__(self, name):
        self.name = name

    def fly(self):
        return f"{self.name} bird can fly"

    def walk(self):
        return f"{self.name} bird can walk"

    def eat(self):
        return "It eats various foods"


class FlyingBird(Bird):
    def __init__(self, name, ration="grains"):
        super().__init__(name)
        self.ration = ration

    def eat(self):
        return f"It eats mostly {self.ration}"

    def __str__(self):
        return f"{self.name} bird can walk and fly"



class NonFlyingBird(Bird):
    def __init__(self, name, ration="fish"):
        super().__init__(name)
        self.ration = ration

    def swim(self):
        return f"{self.name} bird can swim"

    def eat(self):
        return "It eats mostly fish"

    def fly(self):
        raise AttributeError(f"'{self.name}' object has no attribute 'fly'")


class SuperBird(FlyingBird, NonFlyingBird):
    def __init__(self, name):
        super().__init__(name)

    def eat(self):
        return super().eat()

    def __str__(self):
        capabilities = ", ".join([method.split()[0] for method in dir(self) if callable(getattr(self, method)) and not method.startswith("__")])
        return f"{self.name} bird can {capabilities}"



p = NonFlyingBird("Penguin", "fish")
print (p.swim())
"Penguin bird can swim"

print (p.eat())
"It eats mostly fish"