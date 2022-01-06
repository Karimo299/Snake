class Snake:
    x = 0
    y = 0
    deltaX = 0
    deltaY = 0
    score = 0
    tail = []

    # Constructor function
    def __init__(self):
        # sets the x and y at the center of the grid
        self.x = 19
        self.y = 14
    
    # Sets the direction of the snake's movment
    def setDir(self, dir):
        self.deltaX = 0
        self.deltaY = 0
        if dir == "UP" and self.deltaX == 0:
            self.deltaY = -1
        elif dir == "DOWN" and self.deltaX == 0:
            self.deltaY = 1
        elif dir == "LEFT" and self.deltaY == 0:
            self.deltaX = -1
        elif dir == "RIGHT" and self.deltaY == 0:
            self.deltaX = 1

    # move the snake accoridng to the direction
    def moveSnake(self):
        self.x += self.deltaX
        self.y += self.deltaY

    # refresh the snake by adding the current postion of the head to the tail and moving the head forward
    def refreshSnake(self):
        self.tail.append({"x": self.getX(), "y": self.getY()}) 
        if len(self.tail) > self.score:
            self.tail.pop(0)
        self.moveSnake()

    def resetSnake(self):
        self.x = 19
        self.y = 14
        self.deltaX = 0
        self.deltaY = 0
        self.tail = []
        self.score = 0
    
    def getScore(self):
        return self.score

    def incrementScore(self):
        self.score +=1

    def getX(self):
        return self.x

    def getY(self):
        return self.y
