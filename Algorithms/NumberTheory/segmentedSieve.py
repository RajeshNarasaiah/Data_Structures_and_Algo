import math

prime = []

"""
SieveOfEratostheneses :
This method finds all the primes less than n.

Algo:
1. Mark[] -> size n, initialized to True
2. for every number > 2 and number^2 < n , mark it's multiple as False
3. all the numbers in mark[] set to True are prime

Time: O(n * log(logn))
Space: O(n) ---> too much.
"""
def SieveOfEratostheneses(n):
    mark = [True] * (n + 1)
    p = 2
    
    while (p * p < n):
        if mark[p] == True:
            for idx in range(p*p, n+1, p):
                mark[idx] = False
                
        p += 1
        
    for idx in range(2, len(mark)):
        if mark[idx] == True:
            print(idx)
            prime.append(idx)
            
            
"""
segmentedSieve:
Drawbacks of SieveOfEratostheneses:
1. uses too much space.
2. Misses caching opportunities.

Idea is instead of going through all the numbers from 0 to n-1, we instead create
segments and mark prime numbers in segments (eg: 0-limit, limit - limit2, limit2 - n)
Segmentd Seive Algo:
1. Generate prime using SieveOfEratostheneses for sqrt(num)
2. Create an array mark[] of size [sqrt(num)...sqrt(num) * 2] and initialize as True
3. For each number in mark, set all miltiples of prime[i] as False
4. Numbers which are not marked are prime in current segment.
"""
def segmentedSieve(num):
    limit = int(math.floor(math.sqrt(num)) + 1)
    SieveOfEratostheneses(limit)
    
    low = limit
    high = limit * 2
    
    while low < num:
        if high >= num:
            high = num
            
        mark = [True for _ in range(limit + 1)]
        
        for idx in range(len(prime)):
            low_lim = (low//prime[idx]) * prime[idx]
            
            if low_lim < low:
                low_lim += prime[idx]
                
            for jdx in range(low_lim, high, prime[idx]):
                mark[jdx - low] = False
                
        for idx in range(low, high):
            if mark[idx - low]:
                print(idx)
                
        low += limit
        high += limit
                
segmentedSieve(100)
