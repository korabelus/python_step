# 0 - functions(methods)


def display_matrix(matrix: list):
    for m_row in matrix:
        for el in m_row:
            print(f'{el:5d}', end='')
        print('')

# 1 - > Create:


rows = int(input('rows = '))
cols = int(input('cols = '))

matrix_a = []
for i in range(rows):
    matrix_a.append([0] * cols)

print(matrix_a)

matrix_b = [([1] * cols) for i in range(rows)]
print(matrix_b)

# 2 - > Print:

display_matrix(matrix_b)


# 3 - > Вложенные генераторы:

matrix_c = [[(i + 1) * (j + 1) for j in range(cols)] for i in range (rows)]
print()
display_matrix(matrix_c)

# 4 - > Выборка элементов:
matrix_d = [matrix_c[i][i] in range(rows)]
for x in matrix_d:
    print(x, end='')
print('')

