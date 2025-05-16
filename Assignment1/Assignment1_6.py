
Num1 = int(input("Enter any number: "))

def CheckNum(Num1):
    if Num1>0:
        print("The number is Positive: ")
    elif Num1<0:
        print("The number is Negative: ")
    else:
        print("The number is Zero: ")

if __name__ == "__main__":
    CheckNum(Num1)
