import math
if __name__ == "__main__":
    print("Distance and Midpoint calculator")

    #Find the distance between two points
    def distance():
        point1_x, point1_y = input("[Distance] What is the first set of points? Use format: \"x, y\"\n").split(", ")
        point2_x, point2_y = input("[Distance] What is the second set of points? Use format: \"x, y\"\n").split(", ")
        point1_x = float(point1_x)
        point1_y = float(point1_y)
        point2_x = float(point2_x)
        point2_y = float(point2_y)
        d = ((point2_x-point1_x) ** 2) + ((point2_y-point1_y) ** 2)
        print("The distance between (", point1_x, ", ", point1_y, ") and (", point2_x, ", ", point2_y, ") is √", d, ", which evaluates to: ")
        dp2 = math.sqrt(d)
        print(dp2, "\n")

    #Find the midpoint given two points
    def midpoint():
        point1_x, point1_y = (input("[Midpoint] What is the first se2t of points? Use format: \"x, y\"\n").split(", "))
        point2_x, point2_y = input("[Midpoint] What is the second set of points? Use format: \"x, y\"\n").split(", ")
        point1_x = float(point1_x)
        point1_y = float(point1_y)
        point2_x = float(point2_x)
        point2_y = float(point2_y)
        #x of midpoint
        midpoint_x = ((point1_x + point2_x) / 2)
        #y of midpoint
        midpoint_y = ((point1_y + point2_y) / 2)
        print("The midpoint of the points (", point1_x, ", ", point1_y, ") and (", point2_x, ", ", point2_y, ")\n", "M = (", midpoint_x, midpoint_y, ")\n")

    #Find point B given midpoint and point A
    def endpoint():
        point1_x, point1_y = input("[Endpoint] What is the known endpoint? Use format: \"x, y\"\n").split(", ")
        midpoint_x, midpoint_y = input("[Endpoint] What is the midpoint? Use format: \"x, y\"\n").split(", ")
        point1_x = float(point1_x)
        point1_y = float(point1_y)
        midpoint_x = float(midpoint_x)
        midpoint_y = float(midpoint_y)
        b1 = float((2*midpoint_x)-point1_x)
        b2 = float((2*midpoint_y)-point1_y)
        print("The missing endpoint 'B' from points M(", midpoint_x, ", ", midpoint_y, ") and A(", point1_x, ", ", point1_y, ") is: \n", "Point B = (", b1, b2, ")\n")

while True:
    menunav = int(input("=======\n1. Find the DISTANCE between two points. \n2. Find the MIDPOINT of two points\n3. Find an ENDPOINT given midpoint and one endpoint\n Select a function: "))
    if menunav==1:
        distance()
    elif menunav==2:
        midpoint()
    elif menunav==3:
        endpoint()