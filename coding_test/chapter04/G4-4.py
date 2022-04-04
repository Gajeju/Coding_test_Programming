# 게임 개발
# 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 갈 곳을 정한다
# 캐릭터의 바로 왼쪽에 방문하지 않은 칸이 있다면 회전 후 이동, 방문하지 않칸이 없다면 회전 후 1번으로
# 네 방향 모두 가본 칸이거나 바다로되어있는 경우 한칸 뒤로 가고 1단계로 돌아간다. 뒤쪽이 바다라면 멈춘다

# 방향과 이동 시뮬레이션에서는 dx, dy로 방향관리를 하는게 유용
# 북 동 남 서

# import sys
# input = lambda : map(int, sys.stdin.readline().strip().split())

# n, m = input()
# loc = list(input())
# filed = [list(input()) for _ in range(m)]
# filed[loc[0]][loc[1]] = 2
# cnt = 1

# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# def turn_left(loc):
#     loc[2] = 3 if loc[2] == 0 else loc[2] - 1
#     return loc

# def move_left(loc):
#     loc[0] = loc[0] + dy[loc[2]]
#     loc[1] = loc[1] + dx[loc[2]]
#     return loc

# while True:
#     tmp = loc.copy()
#     for _ in range(4):
#         tmp = move_left(tmp)
#         tmp = turn_left(tmp)

#         if filed[tmp[0]][tmp[1]] == 1 or filed[tmp[0]][tmp[1]] == 2:
#             loc[2] = tmp[2]
#             tmp = loc.copy()
#             continue
#         else:
#             cnt+=1
#             loc = tmp
#             filed[tmp[0]][tmp[1]] = 2
#             print(tmp)
#             break
#     else:
#         tmp = turn_left(tmp)
#         tmp = move_left(tmp)
#         tmp = turn_left(tmp)
#         tmp = turn_left(tmp)
#         tmp = turn_left(tmp)
#         if filed[tmp[0]][tmp[1]] == 1:
#             break
#         else:
#             loc = tmp
    
# print(cnt)


n, m = map(int, input().split())
d = [[0] * m for _ in range(n)]
x, y, direction = map(int, input().split())
d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dx[direction]

    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)