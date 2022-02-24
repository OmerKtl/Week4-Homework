import sys
import math

def addition(x,y):
    try:
        x=float(x)
        y=float(y)  
        print("\n",x,"+",y,"=",math.ceil(x+y),"\n")
    except:            
        print("\nInvalid enterance...")
        text1=str(sys.exc_info()[0])
        print(text1.split("'")[1],"\n") 
def subtraction(x,y):
    try:
        x=float(x)
        y=float(y)  
        print("\n",x,"-",y,"=",math.ceil(x-y),"\n") 
    except:            
        print("\nInvalid enterance...")
        text1=str(sys.exc_info()[0])
        print(text1.split("'")[1],"\n") 
def multiplication(x,y):
    try:
        x=float(x)
        y=float(y)  
        print("\n",x,"X",y,"=",math.ceil(x*y),"\n") 
    except:            
        print("\nInvalid enterance...")
        text1=str(sys.exc_info()[0])
        print(text1.split("'")[1],"\n")
def division(x,y):
    try:
        x=float(x)
        y=float(y) 
        print("\n",x,"/",y,"=",math.ceil(x/y),"\n") 
    except:            
        print("\nInvalid enterance...")
        text1=str(sys.exc_info()[0])
        print(text1.split("'")[1],"\n")