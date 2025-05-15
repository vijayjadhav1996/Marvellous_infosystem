import Arithmetic

def main():
    a = int(input("Enter first Number: "))
    b = int(input ("Enter second Number: "))

    print("Addition of two numbers is: ",Arithmetic.Add(a,b))
    print("Substraction of two numbers is: ",Arithmetic.Sub(a,b))
    print("Multiplication of two numbers is: ",Arithmetic.Mult(a,b))
    print("Division of two number is: ",Arithmetic.Div(a,b))

if __name__ == "__main__":
    main()