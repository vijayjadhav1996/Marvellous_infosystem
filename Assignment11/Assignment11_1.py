def num(n):
    if n < 1:
        return
    num(n - 1)     
    print(n, end=" ")

n = int(input("Enter number: "))
num(n)
