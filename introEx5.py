#5.	Gets the coordinates for two points from the user and computes the distance.
# Round your answer to two decimal places.

print("Enter the coordinate of one point")
X1 = input("X1 = ")
Y1 = input("Y1 = ")

print ("Enter the coordinate of another point")
X2 = input("X2 = ")
Y2 = input("Y2 = ")

Distance = ((int(X2)-int(X1))**2) * ((int(Y2)-int(Y1))**2)**0.5
print("The Distance between enter co-ordinates is " + str(Distance.__round__(2)))


