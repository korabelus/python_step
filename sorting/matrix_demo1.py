M1 = [
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [11, 22, 33, 44],
]

print(M1)
print(M1[1][2])

# 2. Создание нулевой матрицы заданного размера:

rows = int(input('enter number of rows: '))
cols = int(input('enter number of columns: '))

M2 = []
for i in range(rows):
    row = [0] * cols
    M2.append(row)

for i in range(rows):
    for j in range(cols):
        print(f'{M2[i][j]:4d}', end='')
    print('')

