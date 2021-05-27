def print_optimal_paren(s, idx, jdx):
    if idx == jdx:
        print('A', idx)
    else:
        print('(')
        print_optimal_paren(s, idx, s[idx][jdx])
        print_optimal_paren(s, s[idx][jdx] + 1, jdx)
        print(')')
        
def matrix_chain_mul(p):
    n = len(p)
    m = [[0 for _ in range(n)] for _ in range(n)]
    s = [[0 for _ in range(n)] for _ in range(n)]
    
    for l in range(2, n):
        for idx in range(1, n - l + 1):
            jdx = idx + l - 1
            m[idx][jdx] = float('inf')
            for kdx in range(idx, jdx):
                q = m[idx][kdx] + m[kdx + 1][jdx] + p[idx - 1] * p[kdx] * p[jdx]
                if q < m[idx][jdx]:
                    m[idx][jdx] = q
                    print(idx, jdx)
                    s[idx][jdx] = kdx
                    
    print(m)
    print(s)
    print_optimal_paren(s, 1, n - 1)
    return m[1][n - 1]
    
p = [30, 35, 15, 5, 10, 20, 25]
print(matrix_chain_mul(p))
                    
