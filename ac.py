def area():
    length = input("What is the length (in whole feet) of the home? ")
    width = input("What is the width (in whole feet) of the home? ")
    area = int(length) * int(width)
    print(f"The area of the home is: {area} square feet.")


def circumference():
    from math import pi
    radius = input("What is the radius of the circle? (please enter whole number only) ")
    circum = ((2 * pi) * int(radius))
    print(f"The circumference of the circle is {circum} of whatever unit of measurement you are using.")