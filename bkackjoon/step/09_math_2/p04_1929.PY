import sys

m, n = map(int, sys.stdin.readline().split())

if m == 1:
    m += 1

for num in range(m, n+1):
    for i in range(2,int(num**0.5) + 1):
        if num % i == 0:
            break
    else: print(num)



# https://www.acmicpc.net/problem/1929