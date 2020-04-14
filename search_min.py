from random import randint

N = 15
A = 10
B = 99

arr = [(randint(A, B)) for i in range(N)]
print(arr)

mini = arr[0]
k = 0
for j in range(1, N):
    if arr[j] < mini:
        mini = arr[j]
        k = j
print(mini)

