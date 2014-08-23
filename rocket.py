__author__ = 'kevinpan'
# from "Classes" section on introtopython.org
import random
from math import sqrt

class Rocket():
    #Rocket simulates a rocket ship for a game or a physics simulation

    def __init__(self, name='Rocket', x=0, y=0, height=1, crew=1): #__init__ is a built-in Python function that is immediately called when an object instance of
    #a class is created. It sets the starting attributes for the object.
    #Each rocket has a starting (x,y) position. If no arguments are passed for x and/or y the default is 0
    #Each rocket has a specific height and crew size
        self.name = name
        self.x = x
        self.y = y
        self.height = height
        self.crew = crew

    def launch(self):
    #launches rocket
        print('3...2...1...Liftoff! %s has launched from position (%d,%d) with a crew of %d.' % (self.name, self.x, self.y, self.crew))
        self.y += 10

    def land(self):
        self.x = 0
        self.y = 0
        print('%s has landed safely.' % self.name)

    def crash(self):
        print('Mayday! Mayday! %s is going down.' % self.name)
        self.y = 0
        self.crew = 0

    def blackbox(self, turn=None):
        blackbox = (self.name, self.x, self.y, turn)
        return blackbox

    def move_up(self, y=1):
    #increment the y position of the rocket
        self.y += y

    def move_down(self, y=1):
        self.y -= y

    def move_right(self, x=1):
        self.x += x

    def move_left(self, x=1):
        self.x -= x

    def move(self, delta_x=0, delta_y=1):
    #move the rocket according to the parameters given; default is to move rocket up one unit
        self.x += delta_x
        self.y += delta_y

    def move_random(self, unit=1):
    #move the rocket in a random direction, can specify the distance of random direction
        num = random.randrange(0, 3)
        if num == 0: self.move_up(unit)
        if num == 1: self.move_down(unit)
        if num == 2: self.move_right(unit)
        if num == 3: self.move_left(unit)

    def get_distance(self, other_rocket):
    #Calculates and returns distance from this rocket to other rocket based on resultant of x & y distances
        distance = sqrt((self.x - other_rocket.x) ** 2 + (self.y - other_rocket.y) ** 2)
        return distance
