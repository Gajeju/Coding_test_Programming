import sys

input = lambda : int(sys.stdin.readline())

n = input()
lst = [input() for _ in range(n)]

print(*sorted(lst, reverse=True))

