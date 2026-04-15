med_cond = input("Does the student have a medical condition (Y/N): ").strip().upper()

if med_cond == "Y": 
    print("You are allowed")
else: 
    attend = int(input("What is the attendence of the student: "))
    
    if attend >= 75:
        print("You are allowed")
    else: 
       print("You are not allowed")
