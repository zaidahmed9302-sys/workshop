a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

d = b*b - 4*a*c

if d > 0:
    print("Two real roots")
elif d == 0:
    print("Equal roots")
else:
    print("Imaginary roots")
