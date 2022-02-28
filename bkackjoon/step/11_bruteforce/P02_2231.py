n = int(input())

for i in range(n+1):
    tot = i
    result = i
    while i > 0:
        tot += i % 10
        i //= 10
    if tot == n:
        break

if result == n:
    print(0)
else:
    print(result)

# 분해합 : n과 각 자리수의 합
# M의 분해합이 N일때 M을 N의 생성자라고 한다
# N의 가장 작은 생성자를 출력

# https://www.acmicpc.net/problem/2231