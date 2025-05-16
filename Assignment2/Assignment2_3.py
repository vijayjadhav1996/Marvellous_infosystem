
n = int(input("Enter the number: "))

def main():

    if n<0:
        print("We cannot define the factorial for Negative numbers: ")
    else:
        fact = 1
        for i in range(1, n+1):
            fact*=i
        print("Factorial of number: ",n,"is: ",fact)

if __name__ == "__main__":
    main()
