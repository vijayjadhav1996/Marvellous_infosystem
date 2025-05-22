
def main():

    num1,num2,num3,num4,num5 = map(int,input("Enter five numbers by giving one space:").split())

    if num1>=num2 and num1>=num3 and num1>=num4 and num1>=num5:
        print("Number is greater: ",num1)
    elif num2>=num1 and num2>=num3 and num2>=num4 and num2>=num5:
        print("The number is greater:", num2)
    elif num3>=num1 and num3>=num2 and num3>=num4 and num3>=num5:
        print("Number is greater: ",num3)
    elif num4>=num1 and num4>=num2 and num4>=num3 and num4>=num5:
        print("number is greater: ", num4)
    else:
        print("Number is greater: ", num5)

if __name__ == "__main__":
    main()