import math

a, b, c = map(int, input().split())

day = (c - b) / (a - b)
day = math.ceil(day)


print(day)

# 높이 V
# 낮에 A 미터
# 밤에 -B 미터
# https://www.acmicpc.net/problem/2869