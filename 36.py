cp = float(input("Enter cost price: "))
sp = float(input("Enter selling price: "))

if sp > cp:
    print("Profit")
elif sp < cp:
    print("Loss")
else:
    print("No Profit No Loss")
