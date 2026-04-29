RowSize = int(input("Enter number of rows: "))
if RowSize%2 == 0: 
    DiamRow = int(RowSize/2)
else: 
    DiamRow = int(RowSize/2)+1

space = DiamRow - 1
for i in range(1, DiamRow + 1): 
    for j in range(1, space + 1): 
        print(end = " ")

    space = space - 1
    num = 1
    for j in range(2*i-1): 
        print(end=str(num))

        num = num + 1

    print()