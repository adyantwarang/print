lower = int(input("Enter the lowest value: "))
upper = int(input("Enter the highest value: "))

print("\nPrime numbers from ", lower, "to", upper, "are: ")

for num in range(lower, upper + 1): 
    if num > 1: 
        for i in range(2, num): 
            if (num % i) == 0: 
                break

        else: 
             print(num)
