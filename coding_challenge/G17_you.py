# 문자열 A가 입력되었을 때 문자열 A가 'You'이면 'Me'라고 출력하고, 그렇지 않으면 'No'라고 출력하는 프로그램을 작성하세요.
import sys

a = sys.stdin.readline().strip()
if a == 'You':
    print('Me')
else:
    print('No')