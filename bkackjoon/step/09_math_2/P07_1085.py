x, y, w, h = map(int, input().split())
li = []

li.append(x)
li.append(w -x)
li.append(y)
li.append(h - y)

print(min(li))


# 현재 위치 (x, y)
# 왼쪽 아래 (0, 0)
# 오른쪽 위 (w, h)
# 입력 (x, y, w, h)

# https://www.acmicpc.net/problem/1085