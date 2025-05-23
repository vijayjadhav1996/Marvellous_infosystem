

from functools import reduce

num = list(map(int,input("Enter list: ").split()))

Value = reduce(lambda x,y: x*y, num) 
print("Result is: ", Value)