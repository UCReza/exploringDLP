import math
import numpy as np
import time

# Size of the data
N = 1_000_000

# Generate random data
data = np.random.randn(N)

# Scalar implementation: calculate exp for each element one by one
start_scalar = time.time()
result_scalar = [math.exp(x) for x in data]
time_scalar = time.time() - start_scalar

# Vectorized NumPy implementation: uses SIMD/vector instructions internally
start_vector = time.time()
result_vector = np.exp(data)
time_vector = time.time() - start_vector

# Print results
print(f"Scalar implementation time: {time_scalar:.4f} seconds")
print(f"Vectorized (NumPy) implementation time: {time_vector:.4f} seconds")
print(f"Speedup: {time_scalar / time_vector:.2f}x faster")
