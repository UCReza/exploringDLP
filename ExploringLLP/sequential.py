import time


size = 100_000_000
a = list(range(size))
b = [0] * size

start = time.time()
for i in range(size):
    b[i] = a[i] * a[i]
end = time.time()

print(f"Sequential Time: {end - start:.2f} seconds")
