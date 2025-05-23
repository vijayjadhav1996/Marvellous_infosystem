


num = list(map(int,input("Enter list: ").split()))

Value = list(filter(lambda num: num %2==0, num)) 
print("Result is: ", Value)