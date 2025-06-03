
def print_stars(n):
    if n == 0:
        return
    print_stars(n - 1)
    print('* ' * n)

num = int(input("Enter number of rows: "))
print_stars(num)
