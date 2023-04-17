import numpy as np

def diagonal_elemets(A):

    m, n = A.shape

    for k in range(n-1, -m, -1):
        diagonal = np.diagonal(A, offset=k)
        if len(diagonal) > 0:
            print(*diagonal)

A = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16],
              [17, 18, 19, 20]])


print(f'{A}\n\n')
diagonal_elemets(A)