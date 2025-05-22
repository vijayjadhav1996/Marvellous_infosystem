
def add(no1,no2):
    Ans = no1 + no2
    return Ans
def Sub(no1, no2):
    Ans = no1 - no2
    return Ans
def Mult(no1, no2):
    Ans = no1 * no2
    return Ans
def Div(no1, no2):
    Ans = no1/no2
    return Ans

def main():
    no1 = int(input("Enter first Number: "))
    no2 = int(input("Enter second number: "))
    print()

    Result = add(no1, no2)
    print("Addition is: ",Result)
    
    Result = Sub(no1, no2)
    print("substraction is: ",Result)

    Result = Mult(no1, no2)
    print("Multiplication is: ",Result)

    Result = Div(no1, no2)
    print("Division is: ",Result)

if __name__ == "__main__":
    main()