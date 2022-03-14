# 자연수들로 이루어진 수열이 있을 때, 이 수열의 합을 구하려고 합니다.
# N개의 자연수가 주어졌을 때, 이 수들의 합을 구하는 프로그램을 만드세요.

import sys

input = lambda : int(sys.stdin.readline())
n = input()
n_list = [input() for _ in range(n)]
print(sum(n_list))