"""
Calculator:
General Information:
I want to use a program which can calculate basic mathematical operations.
Acceptance Criteria:
* The calculator must support the Addition, Subtraction, Multiplication and Division operations.
* All operations must be in a different module as method.
* Operations must define with two float numbers as parametres.
* Use math.ceil() for all results.
* Create a menu to choose an operation.
* User can choose invalid options, so you must handle all possible error. (Use try except :))
* Inform user what type of error occured (TypError, ValueError etc.)
* This process must continue until user want to quit from calculator
"""
import sys
import calculator_modules as cm
while True:
    try:
        choose=int(input("Please Select an Operation..\nAddition-->(1)\nSubtraction-->(2)\nMultiplication-->(3)\nDivision-->(4)\nEXIT-->(5)\n--> "))
        if choose not in range(1,6):
            print("\nInvalid operation, Try again...\n")
    except:
        print("\nInvalid Operation, Try again... ")
        text1=str(sys.exc_info()[0])
        print(text1.split("'")[1],"\n")
    else:
        if choose==5:
            print("Good Bye!")
            break        
        elif choose==1:
            x=input("Enter first number :")
            y=input("Enter second number :")
            cm.addition(x,y)
        elif choose==2:
            x=input("Enter first number :")
            y=input("Enter second number :")
            cm.subtraction(x,y)              
        elif choose==3:
            x=input("Enter first number :")
            y=input("Enter second number :")
            cm.multiplication(x,y)
        elif choose==4:
            x=input("Enter first number :")
            y=input("Enter second number :")
            cm.division(x,y)