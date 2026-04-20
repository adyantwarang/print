string1 = input("Enter your own string: ")

string2=('')

for i in string1: 
    string2 = i + string2

print("\nOrignal string: ",string1)
print("Reversed string: ",string2)