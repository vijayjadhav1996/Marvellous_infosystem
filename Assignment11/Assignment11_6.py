
def sum_of_num(n):
    if n == 1:
        return 1
    return n + sum_of_num(n - 1)

# Example usage
num = int(input("Enter a positive integer: "))
print("Sum of numbers from 1 to", num, "is:", sum_of_num(num))
