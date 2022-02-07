n = list(map(int, input().split()))

n[1] -= 45
if n[1] < 0:
    n[0] -= 1
    n[1] += 60

if n[0] == -1:
    n[0] = 23

print(n[0], n[1])



# https://www.acmicpc.net/problem/2884