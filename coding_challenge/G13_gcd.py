# 최대공약수란 어떤 두 개 이상의 자연수들이 있을 때, 두 수의 공통된 약수 중 가장 큰 수를 말합니다.
# 서로 다른 두 자연수 N, M이 주어졌을 때, 두 수의 최대공약수를 출력하는 프로그램을 만드세요.

import sys
input = lambda : sys.stdin.readline()

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a%b)

a, b = map(int, input().split())
print(gcd(a,b))