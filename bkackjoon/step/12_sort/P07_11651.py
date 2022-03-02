import sys

n = int(sys.stdin.readline())
coords = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
coords.sort(key= lambda x:[x[1], x[0]])

for coord in coords:
    print(*coord)


# 2중 조건 정렬

# https://www.acmicpc.net/problem/11651