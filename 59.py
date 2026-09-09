a = int(input("Enter a: "))
b = int(input("Enter b: "))

x, y = a, b
while y != 0:
    x, y = y, x % y

gcd = x
lcm = (a * b) // gcd

print("LCM =", lcm)
