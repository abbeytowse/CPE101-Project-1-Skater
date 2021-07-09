# Project 1
#
# Name: Abbey Towse
# Date: 04/07/2021
# Instructor: Turner
# Section: 11


from funcs import *


def main():
    pounds = input("How much do you weigh (pounds)? ")
    massSkater = poundsToKG(float(pounds))

    distance = input("How far away is your professor (meters)? ")
    velocityObject = getVelocityObject(float(distance))

    object = input("Will you throw a rotten (t)omato, banna cream (p)ie "
                   "(r)ock, lawn (g)nome, or (l)ight saber? ")
    massObject = getMassObject(object)

    velocitySkater = getVelocitySkater(massSkater, massObject, velocityObject)
    formattedVelocitySkater = "{:.3f}".format(velocitySkater)
    # Code for formatting decimal places from kite.com
    floatFormattedVelocitySkater = float(formattedVelocitySkater)

    print()
    print("Nice throw!", end=" ")
    # Code to print without new line from geeksforgeeks.org

    # Output varies based on user input
    if massObject <= 0.1:
        print("You're going to get an F!")
    elif 0.1 < massObject <= 1.0:
        print("Make sure your professor is OK.")
    elif 1.0 < massObject:
        if float(distance) < 20:
            print("How far away is the hospital?")
        elif float(distance) >= 20:
            print("RIP professor.")

    print("Velocity of skater:", floatFormattedVelocitySkater, "m/s")

    # Output varies based on user input
    if velocitySkater < 0.2:
        print("My grandmother skates faster than you!")
    if velocitySkater >= 1.0:
        print("Look out for that railing!!!")


if __name__ == '__main__':
    main()
