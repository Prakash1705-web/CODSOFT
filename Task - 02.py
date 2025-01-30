def add(a,b): 
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a/b

while True:
    print("\n Simple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    ch = int(input("Enter your choice : "))

    if ch == 1:
        print("\n")
        print("\t Addition")
        a = float(input("Enter the number : "))
        b = float(input("Enter the number : "))
        print("The answer : ",add(a,b))

    elif ch == 2:
        print("\n")
        print("\t Subtration")
        a = float(input("Enter the number : "))
        b = float(input("Enter the number : "))
        print("The answer : ",sub(a,b))

    elif ch == 3:
        print("\n")
        print("\t Multiplication")
        a = float(input("Enter the number : "))
        b = float(input("Enter the number : "))
        print("The answer : ",mul(a,b))
       

    elif ch == 4:
        print("\t Division")
        a = float(input("Enter the number : "))
        b = float(input("Enter the number : "))
        print("The answer : ",div(a,b))
        print("\n")

    elif ch == 5 :
        print("\t\t Thankyou")
        print("\n")
        break


    else:
        print("Enter the valid choice")
        print("\n")

