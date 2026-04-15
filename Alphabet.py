# Function to check if a single character is an alphabet
def check_alphabet(char):
    if char.isalpha():
        print(f"'{char}' is an alphabet.")
    else:
        print(f"'{char}' is not an alphabet.")

# Testing the function
char_input = input("Enter a character: ")

# Ensure only one character is being checked
if len(char_input) == 1:
    check_alphabet(char_input)
else:
    print("Please enter exactly one character.")




