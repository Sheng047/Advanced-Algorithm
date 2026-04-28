import time

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

rounds = 10
times = []

for r in range(rounds):
    t1 = time.time_ns()

    a = factorial(50)
    b = factorial(100)
    c = factorial(200)

    t2 = time.time_ns()

    T = t2 - t1
    times.append(T)

    print(f"Round {r+1}: {T} ns")

avg_time = sum(times) / rounds
print(f"\nAverage Time: {avg_time:.2f} ns")