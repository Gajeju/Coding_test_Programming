x_list = []
y_list = []

for i in range(3):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

for x in x_list:
    if x_list.count(x) == 1:
        rest_x = x

for y in y_list:
    if y_list.count(y) == 1:
        rest_y = y

print(rest_x, rest_y)

# 세 점이 주어질 때 직사각형을 만들기 위한 네 번째 점
# 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 덩수
# https://www.acmicpc.net/problem/3009