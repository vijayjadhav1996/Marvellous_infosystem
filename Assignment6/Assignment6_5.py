def main():
    num = int(input("Enter number: "))
    print()

    i = 2
    if num > 1:
        while i < num and num % i != 0:
            i += 1

        if i == num:
            print("Prime number ")
        else:
            print("It's not a prime number ")
    else:
        print("Not a prime number ")

if __name__ == "__main__":
    main()
