import numpy as np
import time

a = np.arange(100_000_000, dtype=np.float32)

start = time.time()
b = a * a
end = time.time()

print(f"Vectorized Time: {end - start:.2f} seconds")