import threading

def evenfactor(n):
    total = 0
    print("EvenFactor thread started")
    for i in range(1, n + 1):
        if n % i == 0 and i % 2 == 0:
            total += i
    print("Sum of even factors of",n,total)
    print("EvenFactor thread finished")

def oddfactor(n):
    total = 0
    print("OddFactor thread started")
    for i in range(1, n + 1):
        if n % i == 0 and i % 2 != 0:
            total += i
    print(f"Sum of odd factors of",n,total)
    print("OddFactor thread finished")

def main():
    num = 11

    T1 = threading.Thread(target=evenfactor, args=(num,), )
    T2 = threading.Thread(target=oddfactor, args=(num,), )

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("exit from main")

if __name__ == "__main__":
    main()
