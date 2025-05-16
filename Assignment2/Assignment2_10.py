def main():
    num = input("Enter a number: ")
    if num.startswith('-'):
        num = num[1:]
    total = 0
    for digit in num:
        total += int(digit)
    print("Sum of digits:", total)

if __name__ == "__main__":
    main()
