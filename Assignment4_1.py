
def main():

    num= int(input("Enter any number: "))
    Square = lambda num:num*num
    result = Square(num)

    print("Power of the number is: ", result)


if __name__ == "__main__":
    main()