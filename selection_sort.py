from random import randint

N = 15
A = 10
B = 99

arr = [(randint(A, B)) for i in range(N)]
print(arr)
for i in range(N - 1):
    mini = arr[i]
    k = i
    for j in range(i, N):
        if arr[j] < mini:
            mini = arr[j]
            k = j
    arr[i], arr[k] = arr[k], arr[i]

print(arr)

