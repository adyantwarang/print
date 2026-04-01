#entering your marks
Physics=int(input("Enter marks of Physics: "))
Maths=int(input("Enter marks of Maths: "))
History=int(input("Enter marks of History: "))
English=int(input("Enter marks of English: "))

#Summing it up
Sum = Physics+Maths+History+English

Perc = (Sum/400)*100
print("Your total percentage is: ")
print(Perc)
