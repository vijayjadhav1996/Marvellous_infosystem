from functools import reduce

user_input = input("Enter numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))

filter = list(filter(lambda x: x % 2 == 0, numbers))
map = list(map(lambda x: x ** 2, filter))
Reduce = reduce(lambda x, y: x + y, map)

# used filter 
print("List after filter :", filter)

# used map
print("List after map :", map)

# Reduce
print("Output of reduce :", Reduce)

