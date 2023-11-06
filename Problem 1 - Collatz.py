n, k = map(int, input().split())
a = list(map(int, input().split()))

for i in range(k):
        for _i in range(n):
            if a[_i] % 2 == 0:
                a[_i] = a[_i] // 2
            else:
                a[_i] = 3 * a[_i] + 1

print(sum(a))
