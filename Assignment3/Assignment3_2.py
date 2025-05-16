def main():
    n = int(input("Enter the number of elements: "))
    numbers = []

    nums = input(f"Enter {n} numbers separated by spaces: ").split()
    for i in range(n):
        numbers.append(int(nums[i]))

    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num

    print("The maximum number is:", max_num)

if __name__ == "__main__":
    main()
