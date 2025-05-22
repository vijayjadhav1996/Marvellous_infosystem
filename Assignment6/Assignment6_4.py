

def main():
    num = int(input("Enter number: "))
    print()
    factorial = 1
    num1 = 1

    while num1 <= num: 
        factorial = factorial * num1
        num1 +=1
    print("Factorial",num," is: ",factorial)
if __name__== "__main__":
    main()