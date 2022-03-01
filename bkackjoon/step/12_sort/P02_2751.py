import sys

n = int(sys.stdin.readline())
li = [int(sys.stdin.readline()) for _ in range(n)]
li.sort()

for num in li:
    print(num)

# https://www.acmicpc.net/problem/2751 