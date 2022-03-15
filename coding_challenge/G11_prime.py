# 소수란 약수가 자기 자신과 1만 존재하는 수를 말합니다.
# 수들의 범위가 주어졌을 때, 그 범위 안에 소수가 몇 개 존재하는지 알아내는 프로그램을 만드세요.

import sys

n = int(sys.stdin.readline())
cnt = 0

for i in range(2,n+1):
    for j in range(2, int(i**(0.5))+1):
        if i % j == 0:
            break
    else:
        cnt += 1

print(cnt)