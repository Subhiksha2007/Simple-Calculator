#Function for adding two numbers
def add(a,b):
    return a+b
#Function for subracting two numbers
def sub(a,b):
    return a-b
#Function for multiplying two numbers
def mul(a,b):
    return a*b
#Function for dividing two numbers
def div(a,b):
    return a/b
#Display arithmetic operations
print("Arithmetic operations are : ")
print("1.Addition")
print("2.Subraction")
print("3.Multiplication")
print("4.Division")
#Get input of two numbers and operation chioce fom user
operation=input("Enter the operation to be performed(1/2/3/4): ")
n1=int(input("Enter the number: "))
n2=int(input("Enter the number: "))
#Performing calculation and display the result
if operation=="1":
       print(f"Sum of {n1}+{n2} = {n1+n2}")
elif operation=="2":
    print(f"Difference of {n1}-{n2} = {n1-n2}")
elif operation=="3":
    print(f"Multiplication of {n1}*{n2} = {n1*n2}")
elif operation=="4":
    print(f"Division of {n1}/{n2} = {n1/n2}")
else:
    print("Invalid input. Try again")
       
