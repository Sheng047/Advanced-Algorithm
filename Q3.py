import time
import threading

def factorial(n):
    result = 1  # Primitive operation (assignment)
    for i in range(1, n + 1):  # Loop runs 'n' times
        result *= i  # Primitive operations per loop (multiplication, assignment)
    return result  # Primitive operation (return)


# Thread worker helper
def worker(n, results, index):
    results[index] = factorial(n)


def run_single_threaded(rounds=10):
    print("=== SINGLE-THREADED EXECUTION ===")
    times = []

    for r in range(rounds):
        t1 = time.time_ns()

        # Sequential execution
        a = factorial(50)
        b = factorial(100)
        c = factorial(200)

        t2 = time.time_ns()

        T = t2 - t1
        times.append(T)
        print(f"Round {r + 1}: {T} ns")

    avg_time = sum(times) / rounds
    print(f"-> Average Single-Threaded Time: {avg_time:.2f} ns\n")


def run_multi_threaded(rounds=10):
    print("=== MULTI-THREADED EXECUTION ===")
    times = []

    for r in range(rounds):
        results = [None, None, None]

        t1 = time.time_ns()

        # Create 3 separate threads
        threads = [
            threading.Thread(target=worker, args=(50, results, 0)),
            threading.Thread(target=worker, args=(100, results, 1)),
            threading.Thread(target=worker, args=(200, results, 2)),
        ]

        # Start threads
        for t in threads:
            t.start()

        # Wait for all threads to complete
        for t in threads:
            t.join()

        t2 = time.time_ns()

        T = t2 - t1
        times.append(T)
        print(f"Round {r + 1}: {T} ns")

    avg_time = sum(times) / rounds
    print(f"-> Average Multi-Threaded Time: {avg_time:.2f} ns\n")

def main():
    ROUNDS = 10
    print("Starting Factorial Performance Tests...\n")

    # Run the tests
    run_single_threaded(ROUNDS)
    run_multi_threaded(ROUNDS)


if __name__ == '__main__':
    main()