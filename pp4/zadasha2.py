import numpy as np
A = np.array([
    [11, 0, 13, 0],
    [0, 22, 0, 24],
    [0, 32, 0, 0],
    [0, 0, 0, 44]
])
rows_indices, cols_indices = np.nonzero(A)
print("Індекси та значення ненульових елементів:")
for r, c in zip(rows_indices, cols_indices):
    print(f"A[{r+1}{c+1}] = {A[r, c]}")