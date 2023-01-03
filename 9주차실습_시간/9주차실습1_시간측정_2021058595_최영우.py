import random as r
import time


def insertion_sort(A):
    n = len(A)
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
            A[j + 1]

def shell_sort(a):
    n = len(a)
    gap = n // 2
    while gap >= 1:
        if (gap % 2) == 0: gap += 1
        for i in range(gap, n):
            j = i
            while j >= gap and a[j] < a[j - gap]:
                j -= gap

        gap = gap // 2


count_ary = [1000, 10000, 12000, 15000]

for count in count_ary:

    arr = [r.randint(10000, 99999) for i in range(count)]

    start = time.time()
    insertion_arr = arr.copy()
    shell_array = arr.copy()
    print(f'데이터 수 : {count}개')

    start = time.time()
    insertion_sort(insertion_arr)
    end = time.time()
    print(f'삽입정렬 실행시간 = {end - start : 10.3f}')

    start = time.time()
    shell_sort(insertion_arr)
    end = time.time()

    print(f'쉘 정렬 시행시간 = {end - start : 10.3f}')
    print()