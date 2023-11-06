def subset_scores(N, K, A):
    MOD = 998244353

    def power(x, y):
        result = 1
        x = x % MOD
        while y > 0:
            if y % 2 == 1:
                result = (result * x) % MOD
            y = y // 2
            x = (x * x) % MOD
        return result

    total_score = 0

    for i in range(1 << N):
        subset_sum = 0
        for j in range(N):
            if (i & (1 << j)) > 0:
                subset_sum += A[j]
        total_score = (total_score + power(subset_sum, K)) % MOD
    
    return total_score


import sys

N1, K1 = map(int, input().split())
A1 = list(map(int, sys.stdin.readline().split()))
print(subset_scores(N1, K1, A1))
