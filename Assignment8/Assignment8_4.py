import threading

def CountSmall(s):
    print("Small thread started")
    print("Thread Name:", threading.current_thread().name)
    print("Thread ID:", threading.get_ident())

    count = 0
    for ch in s:
        if ch.islower():
            count += 1
            print(ch, end=' ')
    print("Total number of lowercase characters:", count)
    print("Small thread finished")

def CountCapital(s):
    print("Capital thread started")
    print("Thread Name:", threading.current_thread().name)
    print("Thread ID:", threading.get_ident())

    count = 0
    for ch in s:
        if ch.isupper():
            print(ch, end=' ')
            count += 1
    print("Total number of uppercase characters:", count)
    print("Capital thread finished")


def CountDigits(s):
    print("Digits thread started")
    print("Thread Name:", threading.current_thread().name)
    print("Thread ID:", threading.get_ident())

    count = 0
    for ch in s:
        if ch.isdigit():
            print(ch, end=' ')  # Display digit character
            count += 1
    print("Total number of digits:", count)
    print("Digits thread finished")
def main():

    vijay = "python123kdkdlDJDJDJ"

    T1 = threading.Thread(target=CountSmall, args = (vijay,) )
    T2 = threading.Thread(target=CountCapital, args = (vijay,))
    T3 = threading.Thread (target = CountDigits, args = (vijay,) )

    T1.start()
    T2.start()
    T3.start()


    T1.join()
    T2.join()
    T3.join()

    print("all threads have completed execution.")

if __name__ == "__main__":
    main()
                   