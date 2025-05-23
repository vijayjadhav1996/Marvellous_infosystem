
s = input("Enter a string: ").replace(" ", "").lower()
print("Palindrome" if (lambda x: x == x[::-1])(s) else "Not a palindrome")
