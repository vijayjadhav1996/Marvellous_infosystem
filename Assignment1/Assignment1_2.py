
Result = int(input("Enter a number"))

def CheckNum(Number):
    if Number % 2 == 0:
        print("The number is Even:")
    else:
        print("The number is Odd")

if __name__ =="__main__":
    CheckNum(Result)