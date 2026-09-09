m = int(input("Enter month number: "))

if m == 2:
    print("28 or 29 days")
elif m in [4, 6, 9, 11]:
    print("30 days")
elif 1 <= m <= 12:
    print("31 days")
else:
    print("Invalid month")
