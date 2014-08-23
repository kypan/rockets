__author__ = 'kevinpan'

import random
from rocket import Rocket

launchpoints = random.sample(range(-5, 5), 5)

flagship = Rocket('Flagship', launchpoints[4], 0, 1, 1)
enterprise = Rocket('Enterprise', launchpoints[0], 0, 1, 50)
dreadnought = Rocket('Dreadnought', launchpoints[1], 0, 1, 10000)
destroyer = Rocket('Destroyer', launchpoints[2], 0, 1, 100)
corvette = Rocket('Corvette', launchpoints[3], 0, 1, 500)

rockets = [flagship, enterprise, dreadnought, destroyer, corvette]
fallenrockets = []

turncount = 0
casualties = 0

for rocket in rockets:
    rocket.launch()

while len(rockets) > 1 and turncount < 300:
    turncount += 1
    print('Turn %d has started' % turncount)
    for rocket in rockets:
        rocket.move_random()
        #print('%s is now at (%d,%d)' % (rocket.name, rocket.x, rocket.y))
    for i in range(len(rockets)):
        if rockets[i].y == 0 and rockets[i].crew != 0:
            fallenrockets.append(rockets[i].blackbox(turncount))
            casualties += rockets[i].crew
            rockets[i].crash()
            print('%s has crash-landed!' % rockets[i].name)
        for j in range(len(rockets)):
            if rockets[i].get_distance(rockets[j]) == 0 and i != j and rockets[i].y != 0:
                print('%s & %s have collided!' % (rockets[i].name, rockets[j].name))
                fallenrockets.append(rockets[i].blackbox(turncount))
                fallenrockets.append(rockets[j].blackbox(turncount))
                casualties += (rockets[i].crew + rockets[j].crew)
                rockets[i].crash()
                rockets[j].crash()
    rockets = [rocket for rocket in rockets if rocket.crew != 0]

print('\nPost-simulation results: \n')
print('Surviving rocket(s): ')
for rocket in rockets:
    print(rocket.name + ' [Final position: (%d,%d)]' % (rocket.x, rocket.y))
print('\nFallen rocket(s): ')
for rocketprofile in fallenrockets:
    print(rocketprofile[0] + ' [Turn %d at (%d,%d)]' % (rocketprofile[3], rocketprofile[1], rocketprofile[2]))
print('\nCasualties: %d' % casualties)
