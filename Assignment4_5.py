
from functools import reduce

def function1(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def function2(n):
    return n * 2

def function3(acc, n):
    return acc if acc > n else n

def main():

    Data = list(map(int, input("Enter numbers by space one: ").split()))

    print("Input Data: ", Data)

    FData = list(filter(function1, Data))

    print("Filter output: ",FData)

    MData = list(map(function2,FData))

    print("Map output: ", MData)

    RData = reduce(function3, MData,1)

    print("Reduce Output: ",RData)

if __name__ == "__main__":
    main()