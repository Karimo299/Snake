import random
class Food:
    x = 0
    y = 0
    def __init__(self, tail):
        self.x = random.randint(0, 39)
        self.y = random.randint(0, 29)
        while {"x": self.x, "y": self.y} in tail:
            self.x = random.randint(0, 39)
            self.y = random.randint(0, 29)


    def getX(self):
        return self.x

    def getY(self):
        return self.y