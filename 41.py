h = int(input("Enter hour: "))
m = int(input("Enter minute: "))

angle = abs(30*h - 5.5*m)

if angle > 180:
    angle = 360 - angle

print("Angle =", angle)
