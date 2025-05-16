
from MarvellousNum import checkprime

def main():
    n = int(input("Enter the number of elements: "))
    
    nums = input(f"Enter {n} numbers separated by spaces: ").split()
    
    if len(nums) != n:
        print(f"Error: Expected {n} numbers but got {len(nums)}.")
        return
    
    total = 0
    for val in nums:
        num = int(val)
        if checkprime(num):
            total += num
    
    print("Addition of all prime numbers is:", total)

if __name__ == "__main__":
    main()
