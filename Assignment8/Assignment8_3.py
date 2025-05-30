import threading

def evenlist(numbers):
    print("Evenlist thread started")
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    print("Sum of even numbers:", total)
    print("Evenlist thread ended")

def oddlist(numbers):
    print("Oddlist thread started")
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
    print("Sum of odd numbers:", total)
    print("Oddlist thread ended")

def main():
    input_list = [10, 15, 20, 25, 30, 35, 40]  

    T1 = threading.Thread(target=evenlist, args=(input_list,))
    T2 = threading.Thread(target=oddlist, args=(input_list,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("Both threads completed execution.")

if __name__ == "__main__":
    main()
