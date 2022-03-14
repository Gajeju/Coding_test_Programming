# 공백을 포함하지 않는 문자열이 하나 주어졌을 때 해당 문자열에 포함되어 있는 문자 'k'의 개수를 출력하는 프로그램을 작성하세요.

import sys
input = lambda  : sys.stdin.readline().strip()

str = input()
print(str.count('k'))
