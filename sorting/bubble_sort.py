from random import randint

N = 15
A = 10
B = 99

arr = [(randint(A, B)) for i in range(N)]
print(arr)

for i in range(N - 1):
    for j in range(N - 1 - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j+1] = arr[j + 1], arr[j]


print(arr)

