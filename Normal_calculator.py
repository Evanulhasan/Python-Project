# Calculator 



print("******************* CALCULATOR *******************")
a = int(input('Enter the First Number here: '))
b = int(input("Enter the Second Number here: "))

# Option
print("Enter the 1 for 'Addition'")
print("Enter the 2 for 'Subtraction'")
print("Enter the 3 for 'Multiplication'")
print("Enter the 4 for 'Division'")
print("Enter the 5 for 'Modulus'")
print("Enter the 6 for 'Exponentiation'")
print("Enter the 7 for 'Floor Division'")

# Take Choice 
while True:
    choice = int(input("Choice a number for 1 to 7: "))
    if choice > 7:
        print("Invalid Input")
    elif choice == 0:
        print("Invalid Input")
    else:
        break
    
if(choice == 1):
    # Addition
    print(f"The value of {a} + {b} is: {a+b}")
    
elif(choice == 2):
    # Subtraction
    print(f"The value of {a} - {b} is: {a-b}")
    
elif(choice == 3):
    # Multiplication
    print(f"The value of {a} * {b} is: {a*b}")

elif(choice == 4):
    # Division 
    print(f"The value of {a} / {b} is: {a/b}")
elif(choice == 5):
    # Modulus 
    print(f"The value of {a} % {b} is: {a%b}")

elif(choice == 6):
    # Exponentiation
    print(f"The value of {a} ** {b} is: {a**b}")
    
elif(choice == 7):
    # Floor division
    print(f"The value of {a} // {b} is: {a//b}")




    