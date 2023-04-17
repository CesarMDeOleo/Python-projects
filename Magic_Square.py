import numpy as np

def is_magic(matrix):

    if matrix.shape[0] != matrix.shape[1]:
        return False

    n = matrix.shape[0]
    magic_sum = n * (n**2 + 1) // 2
    row_sums = np.sum(matrix, axis=1)
    col_sums = np.sum(matrix, axis=0)
    diag_sum1 = np.sum(np.diag(matrix))
    diag_sum2 = np.sum(np.diag(np.fliplr(matrix)))

    if (
        np.all(row_sums == magic_sum)
        and np.all(col_sums == magic_sum)
        and diag_sum1 == magic_sum
        and diag_sum2 == magic_sum
    ):
        return (True, 0)
    elif np.all(row_sums == magic_sum) and np.all(col_sums == magic_sum):
        return (True, 1)
    elif np.sum(np.unique(matrix)) != n * (n**2 + 1) // 2:
        return (True, 2)
    return False


in_mat_0 = np.array([[2, 16, 13, 3], [11, 5, 8, 10], [7, 9, 12, 6], [14, 4, 1, 15]])

in_mat_2 = np.array(
    [
        [29**2, 1**2, 47**2],
        [41**2, 37**2, 1**2],
        [23**2, 41**2, 29**2],
    ]
)

print(is_magic(in_mat_0))
print(is_magic(in_mat_2))