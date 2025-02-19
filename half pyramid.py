print("Creating half pyramids with starts (*)")
n= int(input("Enter the number of rows in the half pyramid: "))

for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print()