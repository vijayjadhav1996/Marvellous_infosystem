def main():
    n = int(input("Enter the number of elements: "))
    numbers = []

    nums = input(f"Enter {n} numbers separated by space: ").split()
    for i in range(n):
        num = int(nums[i])
        numbers.append(num)

    total = 0
    for num in numbers:
        total += num

    print("The total sum is:", total)

if __name__ == "__main__":
    main()












if __name__ == "__main__":
    main()