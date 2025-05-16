

def main():
    n = int(input("Enter any number: "))
    total = 0
    factors = []
    for i in range(1, n):
        if n % i == 0:
            total +=i
            factors.append(i)
    print("Factors of: ",n,"are: ", factors)
    print("Sum of Factors: ",n, "is: ",total)

if __name__ == "__main__":
    main()