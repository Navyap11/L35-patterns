row_size= int(input("Enter the number of rows: "))
if row_size%2==0:
    hdr= int(row_size/2)
else:
    hdr= int((row_size/2)+1)
space=hdr-1

for i in range(1,hdr+1):
    for j in range (1, space+1):
        print(end=" ")
    space= space-1
    num=1
    for j in range(2*i-1):
        print(end=str(num))
        
        num=num+1
    print()
space=1

for i in range(1,hdr):
    for j in range(1, space+1):
        print(end=" ")
    space=space+1
    num=1
    for j in range(1, 2*(hdr-1)):
        print(end=str(num))
        
        num=num+1
    print()