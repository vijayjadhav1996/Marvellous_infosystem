

def main():
    n=1
    total = 0
    while n<=100:
        if n % 2 ==0:
            total = total + n
        n +=1
    print()
    print("Sum of Even numbers till 100 is: ", total)
    
if __name__ == "__main__":
    main()