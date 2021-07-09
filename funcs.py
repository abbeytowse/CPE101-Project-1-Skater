import math


def poundsToKG(pounds):
    # Input type: string
    # Output type: float
    # Coverts pounds to kilograms
    massSkater = pounds * 0.453592
    return massSkater


def getMassObject(object):
    # Input type: string
    # Output type: float
    # Gives object mass based on object choice
    if object == 't':
        return 0.1
    elif object == 'p':
        return 1.0
    elif object == 'r':
        return 3.0
    elif object == 'g':
        return 5.3
    elif object == 'l':
        return 9.07
    else:
        return 0.0


def getVelocityObject(distance):
    # Input type: string
    # Output type: float
    # Gives object velocity based on distance
    velocityObject = math.sqrt(((9.8 * distance) / 2))
    return velocityObject


def getVelocitySkater(massSkater, massObject, velocityObject):
    # Input types: floats
    # Output type: float
    # Calculates skater's velocity based on skater's mass, object's mass,
    # and object's velocity
    velocitySkater = ((massObject * velocityObject) / massSkater)
    return velocitySkater
