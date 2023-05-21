import math
from decimal import Decimal
if __name__ == "__main__":
    print("Distance and Midpoint calculator")


    def distance():
        #user defines points
        x1, y1 = input("[Distance] What is the first set of points? Use format: \"x, y\"\n").split(", ")
        x2, y2 = input("[Distance] What is the second set of points? Use format: \"x, y\"\n").split(", ")
        # Convert to decimal
        x1 = float(x1)
        y1 = float(y1)
        x2 = float(x2)
        y2 = float(y2)
        d = ((x2-x1) ** 2) + ((y2-y1) ** 2)
        #Prints answer with
        print("The distance between (", x1, ", ", y1, ") and (", x2, ", ", y2, ") is √", d, ", which evaluates to: ")
        #Evalutes the square root
        dp2 = math.sqrt(d)
        print(dp2, "\n")

#Find midpoint given two points
def midpoint():
    #user defines points
    x1, y1 = input("[Midpoint] What is the first set of points? Use format: \"x, y\"\n").split(", ")
    x2, y2 = input("[Midpoint] What is the second set of points? Use format: \"x, y\"\n").split(", ")
    # Convert to decimal
    x1 = float(x1)
    y1 = float(y1)
    x2 = float(x2)
    y2 = float(y2)
    # Find x of midpoint
    m1 = ((x1 + x2) / 2)
    # Find y of midpoint
    m2 = ((y1 + y2) / 2)
    #result:
    print("The midpoint of the points (", x1, ", ", y1, ") and (", x2, ", ", y2, ")\n", "M = (", m1, m2, ")\n")



#Find point B given midpoint and point A
def endpoint():
    #user defines points
    x1, y1 = input("[Endpoint] What is the known endpoint? Use format: \"x, y\"\n").split(", ")
    m1, m2 = input("[Endpoint] What is the midpoint? Use format: \"x, y\"\n").split(", ")
    # Convert to decimal
    x1 = float(x1)
    y1 = float(y1)
    m1 = float(m1)
    m2 = float(m2)
    if x1 > 0:
        # Finding b1: If x1 is positive, add it to 2 * m1
        b1 = (2*m1)-x1
    else:
        # if x1 is neg, subtract it from 2 * m1
        b1 = (2*m1)-x1
    #Finding b2
    if y1 > 0:
        #if y1 is pos, add it to 2 * m2
        b2 = (2*m2)-y1
    else:
        #if y1 is neg, subtract it from 2 * m2
        b2 = (2*m2)-y1

    b1 = float(b1)
    b2 = float(b2)
    print("The missing endpoint 'B' from midpoint (", m1, ", ", m2, ") and (", x1, ", ", y1, ") is: \n", "Point B = (", b1, b2, ")\n")


while True:
    menunav = int(input("=======\n1. Find the DISTANCE between two points. \n2. Find the MIDPOINT of two points\n3. Find an ENDPOINT given midpoint and one endpoint\n Select a function: "))
    if menunav == 1:
        distance()
    elif menunav == 2:
        midpoint()
    elif menunav == 3:
        endpoint()