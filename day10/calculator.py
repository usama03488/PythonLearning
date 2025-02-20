def add(a1,a2):
    print(f"values {a1} and second {a2}")
    return a1+a2
def Subtract(a1,a2):
    return a1-a2
def Multiply(a1,a2):
    return a1*a2
def divide(a1,a2):
    if(a2!=0):
        return a1/a2
    else:
        return 0
def Take_input():
    n1 = 0
    n2 = 0
    Ismore=True
    while(Ismore==True):
        n1 = int(input("Enter First number"))
        print("""+
            -
            *
            /""")
        operator = input("Pick an operation")
        n2 = int(input("Enter the second number"))
        calculator = {'+': add, '-': Subtract, '*': Multiply, '/': divide}
        print(calculator[operator](n1, n2))
        data=input("Type Y if you need more calculation").upper()
        if(data!= "Y" ):
            Ismore=false





Take_input()

