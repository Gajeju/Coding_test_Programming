t = int(input())

for _ in range(t):
    n, s = input().split()
    n = int(n)
    p = ''

    for c in s:
        p += c * n
    print(p)



# https://www.acmicpc.net/problem/2675