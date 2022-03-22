# 중학생인 세아는 아직 제곱의 개념을 바르게 이해하지 못했습니다.
# 세아를 위해 정수 두 개 A, B를 입력받아 A의 B제곱을 출력하는 프로그램을 작성하세요.
import sys

a, b = map(int, sys.stdin.readline().split())
print(a ** b)