# 공백을 포함하는 두 개의 문장이 줄바꿈을 기준으로 입력 됩니다. 이 두 문장을 줄바꿈을 기준으로 그대로 출력하는 프로그램을 작성하세요.

import sys
input = lambda : sys.stdin.readline().strip()

n_list = [input() for _ in range(2)]
print(*n_list, sep='\n')