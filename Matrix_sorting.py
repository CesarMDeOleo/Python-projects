def sort_matrix(in_mat, mode_select=0):
    new_list = in_mat.copy()
    if mode_select == 0:
        for row in new_list:
            row.sort()
    elif mode_select == 1:
        for i in range(len(new_list[0])):
            col = [new_list[j][i] for j in range(len(new_list))]
            col.sort(reverse=True)
            for j in range(len(new_list)):
                new_list[j][i] = col[j]
    return new_list


A = [[3, 6, -4, 6], [-8, -4, -1, -7], [-5, 3, -1, 9]]


print(sort_matrix(A))