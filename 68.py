n = abs(int(input("Enter number: ")))

largest = 0
smallest = 9

while n > 0:
    d = n % 10
    if d > largest:
        largest = d
    if d < smallest:
        smallest = d
    n //= 10

print("Largest =", largest)
print("Smallest =", smallest)
