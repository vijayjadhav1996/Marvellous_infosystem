

def main():
    a,b,c = map(int,input("Enter three numbers by giving one space:").split())

    if a>=b and a>=c:
        print("Largest number is : ",a)
    elif b>=a and b>=c:
        print("Largest number is : ",b)
    else:
        print("Largest number is : ",c)

if __name__ == "__main__":
    main()