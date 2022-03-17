# 정수 A가 입력되었을 때 컴퓨터 시스템에서 정수 A를 참으로 인식한다면 0(거짓)을 출력하고, 그렇지 않으면 1(참)을 출력하는 프로그램을 작성하세요.
import sys

n = int(sys.stdin.readline())
print(0 if n else 1)