import multiprocessing
import time

def square_list(numbers):
    result = [n * n for n in numbers]
    print(f"Squares: {result}")

nums = [1, 2, 3, 4, 5]
result = square_list(nums)

def main():
    print("Demonstration of parallel execution:")
    start_time = time.time()

    P1 = multiprocessing.Process(target=square_list, args=([10],))
    P1.start()
    P1.join()

    end_time = time.time()
    print("Time required for execution: ", end_time - start_time)
    print("End of main.")

if __name__ == "__main__":
    main()
