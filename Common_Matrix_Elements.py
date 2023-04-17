import numpy as np

def common_elements(A):
    row = set(A[0])
    for i in range(1, len(A)):
        row = row.intersection(set(A[i]))

    A_T = []
    for i in range(len(A[0])):
        col = []
        for j in range(len(A)):
            col.append(A[j][i])
        A_T.append(col)

    col = set(A_T[0])
    for i in range(1, len(A_T)):
        col = col.intersection(set(A_T[i]))

    print(f'The common elements between the rows are {sorted(list(row))}\
 and the common elements between the columns are {sorted(list(col))}.\n')

A = np.array([[7, 1, 5, 6], [2, 6, 1, 1], [6, 1, 7, 2], [6, 6, 3, 1], [5, 5, 6, 1], [3, 6, 7, 1]])

print(f"\n{A}\n")

common_elements(A)