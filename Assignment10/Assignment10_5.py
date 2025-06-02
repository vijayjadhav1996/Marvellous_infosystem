from functools import reduce

user_input = input("Enter numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

filter_prime = list(filter(is_prime, numbers))
map_double = list(map(lambda x: x * 2, filter_prime))
Reduce_max = reduce(lambda x, y: x if x > y else y, map_double)

# used filter 
print("List after filter :", filter_prime)

# used map
print("List after map :", map_double)

# Reduce
print("Output of reduce :", Reduce_max) 
