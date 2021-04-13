"""
Given an integer array, find the maximum sum among all subarrays possible.

time: O(nLogn)
"""
def max_crossing_subarray(A, low, mid, high):
    left_sum, right_sum = float('-inf'), float('-inf')
    s        = 0
    for idx in range(mid, low, -1):
        s += A[idx]
        if s > left_sum:
            left_sum = s
            
    s = 0
    for jdx in range(mid + 1, high):
        s += A[jdx]
        if s > right_sum:
            right_sum = s
                
    return max(left_sum, right_sum, left_sum + right_sum)
        
def max_subarray(A, low, high):
    #Base case
    if low == high:
        return A[low]
    else:
        mid = (low + high) // 2
        return max( max_subarray(A, low, mid), max_subarray(A, mid + 1, high), max_crossing_subarray(A, low, mid, high) )
                        
arr = [2, -4, 1, 9, -6, 7, -3]
print(max_subarray(arr, 0, len(arr) - 1))        
