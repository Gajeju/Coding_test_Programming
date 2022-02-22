import math

t = int(input())

for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(float, input().split())

    distance = math.sqrt((x1 -  x2) ** 2 + (y1 - y2) ** 2)
    r_sum = r1 + r2

    if distance == 0 and r1 == r2 :
        print(-1)
    elif abs(r1-r2) == distance or r1 + r2 == distance:
        print(1)
    elif abs(r1-r2) < distance < (r1+r2): 
        print(2)
    else:
        print(0)


# x1, y1, x2, y2, r1, r2 입력으로 주어진다
# x1, y1 (조규현) x2, y2 (백승환)
# r1 조규현이 계산한 류재명과의 거리
# r2 백승환이 계산한 류재명과의 거리
# x1, y1 반지름 r1
# x2, y2 반지름 r2
# 두 붠이 겹치는 수 (0 ~ 2)

# 1. 두 점의 위치가 같으면 -1
# 2. 두 점의 거리를 구한다
# 3. r1 + r2 가 거리보다 길면 0 같으면 1 가까우면 2


# https://www.acmicpc.net/problem/1002