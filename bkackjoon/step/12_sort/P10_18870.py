import sys

n = int(sys.stdin.readline())
coords = list(map(int, sys.stdin.readline().split()))

comp = {}
coords_sort = sorted(list(set(coords)))

for i in range(len(coords_sort)):
    comp[coords_sort[i]] = i

for i in range(n):
    print(comp[coords[i]], end=' ')





# 좌표 앞축
# 최솟값이 0이 된다
# 대소관계에 따라 1씩 차이를 낸다

# https://www.acmicpc.net/problem/18870