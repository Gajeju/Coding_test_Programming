# 수연이네 반 칠판 앞에 누군가 큰 거울을 놓았습니다. 이때부터 칠판에 쓴 글씨나 숫자는 모두 좌우가 상반된 형태로 보입니다.
# 예를 들어 214는 412로 보입니다. 칠판에 서로 다른 두 세 자리 숫자가 쓰여졌을 때, 거울에 비춰진 두 숫자 중 더 큰 숫자를 출력하세요.

import sys
input = lambda: sys.stdin.readline().strip()

a, b = input().split()
a = int(a[::-1])
b = int(b[::-1])

print(a if a > b else b)