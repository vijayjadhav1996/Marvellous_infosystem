

Num1 = int(input("Enter any number: "))

def Divisible(Num1):
    if Num1 % 5 == 0:
        return True
    else:
        return False
Result = Divisible(Num1)
print("The number is:",Result)

if __name__ =="__main__":
    Divisible(Num1)