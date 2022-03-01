import sys

n = int(sys.stdin.readline())

n_list = [0] * 10001

for i in range(n):
    n_list[int(sys.stdin.readline())] += 1

for i in range(len(n_list)):
    if n_list[i]:
        for j in range(n_list[i]):
            print(i)


# https://www.acmicpc.net/problem/10989