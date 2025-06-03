def countz(n):
    if n<10:
        if n==0:
            return 1
        else:
            return 0
    small=countz(n//10)
    if n%10==0:
        return small+1
    else:
        return small


n = int(input("Enter number: "))
print(countz(n))