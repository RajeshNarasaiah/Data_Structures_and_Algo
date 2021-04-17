"""
Implementation of counting sort. Stable sort.
Time: O(n)
"""
def countingSort(A, B, k):
    C = [0] * k
    for idx in range(0, len(A)):
        C[A[idx]] += 1

    for idx in range(1, len(C)):
        C[idx] += C[idx - 1] 
    
    for jdx in range(len(A) - 1, -1, -1):
        key = A[jdx]
        print('key: ', key, 'C[key]', C[key])
        B[C[key] - 1] = key  #note : B[C[key] - 1] to avoid index out of bounds
        C[key] -= 1
        
A = [2,3,4,0,2,3,0,3]
B = [0] * len(A)
countingSort(A, B, 6)
print(B)
    
