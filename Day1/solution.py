import sys
import string
from collections import Counter


def main(filename):
    print filename

    startingPoint = [0, 0]

    visitedLocations = []

    twice = []

    visitedLocation = startingPoint[:]
    visitedLocations.append(visitedLocation)

    facingDirection = 'N'

    with open(filename) as f:
        lines = f.readlines()

    path = list(map((lambda instruction: instruction.strip()), string.split(lines[0], ',')))

    for instruction in path:

        rotation = instruction[0]
        steps = instruction[1:]

        if rotation == 'R':
            if facingDirection == 'N':
                facingDirection = 'E'
            elif facingDirection == 'E':
                facingDirection = 'S'
            elif facingDirection == 'S':
                facingDirection = 'W'
            else:
                facingDirection = 'N'
        else:
            if facingDirection == 'N':
                facingDirection = 'W'
            elif facingDirection == 'E':
                facingDirection = 'N'
            elif facingDirection == 'S':
                facingDirection = 'E'
            else:
                facingDirection = 'S'

        if facingDirection == 'N':
            #startingPoint[1] = startingPoint[1] + int(steps)
            for x in range(int(steps)):
                startingPoint[1] = startingPoint[1] + 1
                visitedLocation = startingPoint[:]
                if visitedLocation in visitedLocations:
                    alreadyVisited = visitedLocation[:]
                    twice.append(alreadyVisited)
                visitedLocations.append(visitedLocation)

        elif facingDirection == 'E':
            #startingPoint[0] = startingPoint[0] + int(steps)
            for x in range(int(steps)):
                startingPoint[0] = startingPoint[0] + 1
                visitedLocation = startingPoint[:]
                if visitedLocation in visitedLocations:
                    alreadyVisited = visitedLocation[:]
                    twice.append(alreadyVisited)
                visitedLocations.append(visitedLocation)

        elif facingDirection == 'S':
            #startingPoint[1] = startingPoint[1] - int(steps)
            for x in range(int(steps)):
                startingPoint[1] = startingPoint[1] - 1
                visitedLocation = startingPoint[:]
                if visitedLocation in visitedLocations:
                    alreadyVisited = visitedLocation[:]
                    twice.append(alreadyVisited)
                visitedLocations.append(visitedLocation)

        else:
            #startingPoint[0] = startingPoint[0] - int(steps)
            for x in range(int(steps)):
                startingPoint[0] = startingPoint[0] - 1
                visitedLocation = startingPoint[:]
                if visitedLocation in visitedLocations:
                    alreadyVisited = visitedLocation[:]
                    twice.append(alreadyVisited)
                visitedLocations.append(visitedLocation)

        #visitedLocation = startingPoint[:]
        #visitedLocations.append(visitedLocation)

    startingPoint = map(lambda coordinate: abs(coordinate), startingPoint)

    print startingPoint
    print sum(startingPoint)

    #print visitedLocations
    #print twice

    beenTwiceAbs = map(lambda coordinate: abs(coordinate), twice[0])

    print beenTwiceAbs
    print sum(beenTwiceAbs)

if __name__ == "__main__":
   main(sys.argv[1])
