n = int(input("Enter number: "))
count = 0

if n == 0:
    count = 1
else:
    n = abs(n)
    while n != 0:
        n //= 10
        count += 1

