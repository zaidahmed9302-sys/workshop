n = int(input("Enter number: "))
original = n
digits = len(str(abs(n)))
total = 0

while n > 0:
    d = n % 10
    total += d ** digits
    n //= 10

if total == original:
    print("Armstrong Number")
else:
    print("Not Armstrong")
