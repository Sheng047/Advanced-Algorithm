import threading
import time

# Factorial function
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Thread worker
def worker(n, results, index):
    results[index] = factorial(n)

# Run 10 rounds
rounds = 10
times = []

for r in range(rounds):
    results = [None, None, None]

    t1 = time.time_ns()

    threads = [
        threading.Thread(target=worker, args=(50, results, 0)),
        threading.Thread(target=worker, args=(100, results, 1)),
        threading.Thread(target=worker, args=(200, results, 2)),
    ]

    # Start threads
    for t in threads:
        t.start()

    # Wait for all threads
    for t in threads:
        t.join()

    t2 = time.time_ns()

    T = t2 - t1
    times.append(T)

    print(f"Round {r+1}: {T} ns")

# Average time
avg_time = sum(times) / rounds
print(f"\nAverage Time: {avg_time:.2f} ns")