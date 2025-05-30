import threading

def SumEven():
    print("Even thread started")
    for i in range(2, 21, 2):
        print("Even Numbers: ",i)
    print("Even thread finished")

def SumOdd():
    print("Odd thread started")
    for i in range(1, 20, 2): 
        print("Odd Numbers: ",i)
    print("Odd thread finished")

def main():

    T1 = threading.Thread(target=SumEven, )
    T2 = threading.Thread(target=SumOdd, )

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("Both threads have completed execution.")

if __name__ == "__main__":
    main()
