# 0 - functions(methods)


def display_matrix(matrix: list):
    for m_row in matrix:
        for el in m_row:
            print(f'{el:5d}', end='')
        print('')

# считывание матрицы из файла


with open('data.txt', 'r', encoding='utf-8') as f:
    rows = int(f.readline())
    columns = int(f.readline())
    print(rows, columns)
    A = [[int(z) for z in f.readline().split()] for i in range(rows)]
    display_matrix(A)

