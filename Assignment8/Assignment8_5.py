import threading
import time

def display_ascending():
    print("Thread1 started")
    for i in range(1, 51):
        print(i, end=' ')
    print("Thread1 finished")

def display_descending():
    print("Thread2 started")
    for i in range(50, 0, -1):
        print(i, end=' ')
    print("Thread2 finished")

def main():
    print("Main thread started")

    t1 = threading.Thread(target=display_ascending, name="Thread1")
    t2 = threading.Thread(target=display_descending, name="Thread2")

    t1.start()
    t1.join()   

    t2.start()
    t2.join()

    print("Main thread finished")

if __name__ == "__main__":
    main()
