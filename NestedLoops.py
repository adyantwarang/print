string = input("Enter string: ")
character = input("Enter character: ")

i = 0
count = 0

while(i<len(string)):

    if(string[i] == character): 

        count = count + 1
    i = i + 1

print("Total number of times", character, "has occured = " , count)
