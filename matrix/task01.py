matrix_a = [
    [12, 14, 67, 45],
    [32, 87, 45, 63],
    [69, 45, 14, 11],
    [40, 12, 35, 15]
]
min_el = matrix_a[0][0]
max_el = matrix_a[0][0]
min_el_i = 0
min_el_j = 0
max_el_i = 0
max_el_j = 0
for i in range(4):
    for j in range(4):
        if min_el > matrix_a[i][j]:
            min_el = matrix_a[i][j]
            min_el_i = i
            min_el_j = j
        if max_el < matrix_a[i][j]:
            max_el = matrix_a[i][j]
            max_el_i = i
            max_el_j = j
print(f'maximum element is {max_el} with indexes i = {max_el_i + 1} and j = {max_el_j + 1}')
print(f'minimum element is {min_el} with indexes i = {min_el_i + 1} and j = {min_el_j + 1}')
