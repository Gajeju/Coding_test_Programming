# 10진수를 입력 받아 8진수와 16진수를 출력하는 프로그램을 작성하세요.
import sys

n = int(sys.stdin.readline())
print(format(n, 'o'), format(n, 'X'))