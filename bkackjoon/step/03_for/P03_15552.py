import sys

n = int(sys.stdin.readline())
n_list = [sum(list(map(int, sys.stdin.readline().split()))) for _ in range(n)]

print(*n_list, sep='\n')


# https://www.acmicpc.net/problem/15552