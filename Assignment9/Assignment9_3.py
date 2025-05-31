import multiprocessing
import math

def compute_factorial(n):
    return math.factorial(n)

def main():
    numbers = [5, 7, 10, 12, 15]

    with multiprocessing.Pool() as pool:
        results = pool.map(compute_factorial, numbers)

    print("Input numbers :", numbers)
    print("Factorials :", results)

if __name__ == "__main__":
    main()
