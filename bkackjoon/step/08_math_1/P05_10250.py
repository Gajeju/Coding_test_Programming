t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())
    x, y = 1, 1    # y층, x호

    while n > h:
        n -= h
        x += 1
    y = n

    if x < 10:
        print(str(y) + '0' + str(x))
    else:
        print(str(y) + str(x))

# 정문으로부터 가장 짧은 거리에 있는 방 선호
# w방이 있는 h층  건물
# 엘리베이터 가장 왼쪽
# 정문 엘리베이터 앞
# 걷는 거리가 같을 때 아래층 선호

# https://www.acmicpc.net/problem/10250