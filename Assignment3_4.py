def main():
    n = int(input("Enter the number of elements: "))
    numbers = []

    nums = input(f"Enter {n} numbers separated by spaces: ").split()
    for i in range(n):
        numbers.append(int(nums[i]))

    target = int(input("Enter the element to search for: "))

    freq = 0
    for num in numbers:
        if num == target:
            freq += 1

    print(f"The frequency of {target} is:", freq)

if __name__ == "__main__":
    main()
