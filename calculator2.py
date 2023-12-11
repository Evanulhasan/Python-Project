# Calculator 



print("******************* CALCULATOR *******************")
a = int(input('Enter the First Number here: '))

# choice operator 

list1 = ["+","-","*","/","%","**","//"]

# Error erase
while True:
    choice = input("Enter operator: ")
    if choice not in list1:
       print("Invalid Input")
    else:           
        break
b = int(input("Enter the Second Number here: "))


    
if(choice == "+"):
    # Addition
    print(f"The value of {a} + {b} is: {a+b}")
    
elif(choice == "-"):
    # Subtraction
    print(f"The value of {a} - {b} is: {a-b}")
    
elif(choice == "*"):
    # Multiplication
    print(f"The value of {a} * {b} is: {a*b}")

elif(choice == "/"):
    # Division 
    print(f"The value of {a} / {b} is: {a/b}")
elif(choice == "%"):
    # Modulus 
    print(f"The value of {a} % {b} is: {a%b}")

elif(choice == "**"):
    # Exponentiation
    print(f"The value of {a} ** {b} is: {a**b}")
    
elif(choice == "//"):
    # Floor division
    print(f"The value of {a} // {b} is: {a//b}")

