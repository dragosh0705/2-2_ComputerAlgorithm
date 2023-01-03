def binary_search(A, key, low, high):
    
    while low<=high:
        middle = (low+high)//2
        if key == A[middle]:
            return middle
        elif key > A[middle]:
            low = middle+1
            if key == middle:
                return low
        elif key <A[middle]:
            high = middle-1
            if key == high:
                return high
        

    if key not in A:
         if key < A[high]:
             for i in range(len(A)):
                 if key < A[i]:
                     return i
         elif key > A[high]:
             return len(a)
            

key = int(input())
a = list(map(int, input().split(' ')))
N = len(a)
print(f' {binary_search(a,key,0,N-1)}')
