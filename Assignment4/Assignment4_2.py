
def main():
    num1, num2 = map(int,input("Enter two numbers by one space: ").split())
    Mult = lambda num1,num2:num1*num2

    result = Mult(num1,num2)
    print("The multiplication is: ",result)

if __name__ == "__main__":
    main()