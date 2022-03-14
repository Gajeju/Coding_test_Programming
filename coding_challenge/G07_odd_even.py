# 정수 A가 입력될 때 A가 짝수인지 홀수인지 판별하는 프로그램을 작성하세요.

import sys
input = lambda : int(sys.stdin.readline().strip())

n = input()
natural = ['E', 'O']
print(natural[n % 2])