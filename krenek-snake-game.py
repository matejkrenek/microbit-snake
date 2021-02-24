from microbit import *
import random

# Class for Snake
class Snake():
    def __init__(self):
        self.length = 1
        self.maxLength = 15
        self.head = [2, 2]
        self.previousPart = []
        self.body = []
        self.directions = ["right", "up", "left", "down"]
        self.currentDirection = "right"

    def NamNamNam(self):
        if self.length < self.maxLength:
            self.length += 1

    def move(self):
        self.body.append(self.head)

        if len(self.body) > self.length - 1:
            self.previousPart = self.body[0]
            self.body.pop(0)

        if(self.currentDirection == "left"):
            self.head = [(self.head[0] - 1) % 5, self.head[1]]

        if(self.currentDirection == "right"):
            self.head = [(self.head[0] + 1) % 5, self.head[1]]

        if(self.currentDirection == "up"):
            self.head = [self.head[0], (self.head[1] - 1) % 5]

        if(self.currentDirection == "down"):
            self.head = [self.head[0], (self.head[1] + 1) % 5]

    def hasSamePosition(self, position):
        return position == self.head or position in self.body

    def display(self):
        display.set_pixel(self.head[0], self.head[1], 9)

        for i in self.body:
            display.set_pixel(i[0], i[1], 7)

# Class for Fruit
class Fruit():
    def __init__(self):
        # generate random position for FRUIT
        self.position = [random.randrange(0, 5), random.randrange(0, 5)]

    def display(self):
        display.set_pixel(self.position[0], self.position[1], 2)

# Class for Game
class Game():
    def __init__(self):
        self.snake = Snake()
        self.initFruit()
        self.score = 0

    def initFruit(self):
        while True:
            self.fruit = Fruit()

            if not self.snake.hasSamePosition(self.fruit.position):
                break

    def updatePosition(self):
        self.snake.move()

        if self.snake.head in self.snake.body or self.snake.head == self.snake.previousPart:
            self.gameOver()

        elif self.snake.head == self.fruit.position:
            self.score += 1
            self.snake.NamNamNam()
            self.initFruit()

    def gameOver(self):
        display.scroll("score: {}".format(self.score))
        sleep(1000)
        reset()

    def handleMovement(self):
        if button_a.was_pressed():
            if self.snake.currentDirection == "":
                self.snake.currentDirection = "right"
            else:
                self.snake.currentDirection = self.snake.directions[(self.snake.directions.index(self.snake.currentDirection) + 1) % len(self.snake.directions)]

        if button_b.was_pressed():
            if self.snake.currentDirection == "":
                self.snake.currentDirection = "right"
            else:
                self.snake.currentDirection = self.snake.directions[(self.snake.directions.index(self.snake.currentDirection) - 1) % len(self.snake.directions)]

    def display(self):
        display.clear()
        self.snake.display()
        self.fruit.display()

# initialize Game
game = Game()

# infinite loop
while True:
    game.handleMovement()
    game.updatePosition()
    game.display()
    sleep(500)