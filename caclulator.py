a=float(input("Enter the first number: "))
b=float(input("Enter the second number: "))

i = True
while(i == True):
    choise=input("choose your operation:")
    if choise=="+":
        print(a+b)
        i = False
    elif choise=="-":
        print(a-b)
        i = False
    elif choise=="*":
        print(a*b)
        i = False
       
    elif choise=="/":
        print(a/b)
        i = False
    else:
        print("wrong symbol")