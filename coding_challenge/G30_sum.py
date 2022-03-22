# 동빈이는 1,000보다 큰 숫자의 덧셈을 할 줄 모릅니다.
# 동빈이를 위해서 두 숫자를 덧셈한 결과를 출력하는 프로그램을 만드세요.
import sys

a, b = map(int, sys.stdin.readline().split())
print(a + b)