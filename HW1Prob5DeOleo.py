number_of_terms = 1000000
cur_term = 0
exp_approximate_value = 0

for n in range(number_of_terms):
    cur_term = (-1)**n / (2*n + 1)
    exp_approximate_value += cur_term


print (f'The approximated value of is {exp_approximate_value*4:.6f}')