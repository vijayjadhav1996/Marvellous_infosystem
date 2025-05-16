
from functools import reduce

def function1(x):
        return 70 <= x <= 90

def function2(x):
        return x + 10

def function3(acc, x):
    return acc * x

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