def main():
    n = int(input("Enter any number: "))

    for i in range(n):
        for j in range(n):
            print("*",end = " ")
        print()

if __name__ == "__main__":
    main()