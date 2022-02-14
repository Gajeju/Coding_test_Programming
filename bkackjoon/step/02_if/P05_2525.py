h, m = map(int, input().split())
ti = int(input())

m += ti
while m >= 60:
    m -= 60
    h += 1

while h >= 24:
    h -= 24

print(h, m)


# 요리 시작 시각과 필요한 시간이 주어질 때 끝나는 시각 출력

# https://www.acmicpc.net/problem/2525