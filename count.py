#taking total amount of input from the user
Amount = int(input("Please enter the amount of withdraw: "))

#calculating number of notes of different denominations
note1 = Amount//100
note2 = (Amount%100)//50
note3 = ((Amount%4100)%50)//20

print("Notes of 100 rupees: ", note1)
print("Notes of 50 rupees: ", note2)
print("Notes of 20 rupees: ", note3)