import sys

t = int(sys.stdin.readline())

for _ in range(t):
    str = sys.stdin.readline().replace(',', ' ')
    print(sum(map(int, str.split())))

# A + B 리턴
# 1,1 형태로 주어짐
# 테스트 케이스

# https://www.acmicpc.net/problem/10953