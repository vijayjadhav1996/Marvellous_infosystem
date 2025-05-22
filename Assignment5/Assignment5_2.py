
def main():
    b = input("Enter your character: ")
    vowels = ['a','e','i','o','u']
    print()

    if b.lower() in vowels:
        print("Entered character is Vowel: ")
    else:
        print("Character is Consonant ")

if __name__ == "__main__":
    main()