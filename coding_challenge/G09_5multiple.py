# 1부터 N까지의 숫자 중에서 5의 배수의 개수를 출력하는 프로그램을 만드세요.

import sys

input = lambda : int(sys.stdin.readline())
n = input()

print(n // 5)