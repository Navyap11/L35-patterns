print("Floyds Triangle")

n= int(input("Enter the amount of rows: "))
number= 1

for m in range (n+1):
    for u in range(m+1):
        print(number, end=" ")
        number= number+1
    print()