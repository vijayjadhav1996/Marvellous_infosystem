
num = list(map(int,input("Enter list: ").split()))

Value = list(map(lambda num: num * 2, num)) 
print("Result is: ", Value)