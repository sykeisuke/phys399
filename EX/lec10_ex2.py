import matplotlib.pyplot as plt
import numpy as np

def fibonacci(n):
    if n == 0: 
        return 0
    elif n == 1: 
        return 1
    else:
        fn_1, fn = 0, 1   # fn_1 = F_{n-1}, fn = F_{n}
        for _ in range(2, n+1):
            fn_1, fn = fn, fn_1 + fn
        return fn

fib_numbers = []
for i in range(31):
    fib_numbers.append(fibonacci(i))

ratios = []
for i in range(1, 30):
    ratios.append(fib_numbers[i+1] / fib_numbers[i])

phi = (1 + np.sqrt(5)) / 2

plt.figure(figsize=(10,4))

# Plots
plt.subplot(1,2,1)
plt.plot(range(31), fib_numbers, marker="o")
plt.title("Fibonacci Numbers")
plt.xlabel("n")
plt.ylabel("F_n")
plt.grid(True)

plt.subplot(1,2,2)
plt.plot(range(1, 30), ratios, marker="o", label=r"$F_{n+1}/F_n$")
plt.axhline(phi, color="red", linestyle="--", label="Golden Ratio")
plt.title("Ratio $F_{n+1}/F_n$")
plt.xlabel("n")
plt.ylabel("Ratio")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

