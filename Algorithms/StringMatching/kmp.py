def compute_prefix_function(P):
    m = len(P)
    LPS = [0] * m
    k = 0
    for q in range(1, m):
        while k > 0 and P[k] != P[q]:
            k = LPS[k]
        if P[k] == P[q]:
            k += 1
        LPS[q] = k
        
    return LPS
    
def kmp(T, P):
    n = len(T)
    m = len(P)
    LPS = compute_prefix_function(P)
    q = 0
    print(LPS)
    for idx in range(0, n):
        while q > 0 and P[q] != T[idx]:
            q = LPS[q - 1]# note q - 1
        if P[q] == T[idx]:
            q += 1
        if q == m:
            print("pattern matched : ", T[q-m : m])
            return
        
    print("Not matched")
pattern = "ababaca"
text    = "ababacavhhj"

kmp(text, pattern)
