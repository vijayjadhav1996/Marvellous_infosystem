


def main():
    n = int(input("Enter the number: "))
    if n<=0:
        print("The number is not prime: ")
        return
    for i in range(2, n):
        if n % i ==0:
            print("The number is not prime cause its reminder is zero and its divisible:")
            return
    print("The number is prime: ")

if __name__ == "__main__":
    main()