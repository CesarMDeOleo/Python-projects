import numpy as np

A = np.arange(2.0, 19.0, 2).reshape(3, 3)
B = np.arange(9.0, 0.0, -1).reshape(3, 3)

print(f"Array A:\n{A}", '\n\n')
print(f"Array B:\n{B}", '\n\n')

A_powered = np.power(A, 2)
print(f'\nThis is how array A looks after being raised by 2 in each element:\n{A}\n')

C = np.multiply(A_powered, B)
print(f'\nThis is how array A looks after being multiplied by array B element wise:\n{C}\n')

D = np.dot(A_powered, B)
print(f'\nThis is how array A looks after being multiplied by array B matrix wise:\n{D}\n')

A[B % 3 == 0] **= 0.5
B[(A % 4 == 0) & (B != 0)] *= -1

print(f'In part B, this is how the answer to the first problem looks like \n{A}\n')
print(f'In part B, this is how the answer to the second problem looks like \n{B}\n')

C_inv = np.linalg.inv(A)
D_inv = np.linalg.inv(B)

C_multiply = np.multiply(C_inv, D_inv)
print(f'\nThis is how the first operation looks after being multiplied by the second operation element wise:\n{C_multiply}')

D_multiply = np.dot(C_inv, D_inv)
print(f'\nThis is how the first operation looks after being multiplied by the second operation matrix wise:\n{D_multiply} \n \n')