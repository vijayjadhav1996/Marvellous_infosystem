
def main():
    length,bridth = map(float,input("Enter area first and then length by giving one space: ").split())
    print()
    Area = length * bridth
    print("Area is: ",Area)

    Perimeter = 2 * (length + bridth)
    print("Perimeter is: ", Perimeter)

if __name__ == "__main__":
    main()