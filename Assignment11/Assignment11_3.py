

def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)

num = int(input("Enter any number: "))

print("Sum of digits:", sum_of_digits(num)) 
