
def main():
    num = int(input("Enter number of rows: "))
    print()
    i = 1
    while i <= num:
        j = 1
        while j <= i:
            print("*", end=" ")
            j += 1
        print()
        i += 1

if __name__ == "__main__":
    main()
