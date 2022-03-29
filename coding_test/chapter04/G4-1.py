# 상하좌우
# n * n 공간에서 상하좌우 이동 후 최종 목적지 출력
# 왼쪽 위가 (1,1) 이며 항상 (1,1)에서 시작
# 공간 바깥으로 넘어가면 무시
# import sys

# n = int(sys.stdin.readline())
# move_list = list(sys.stdin.readline().strip().split())
# start = [1,1]

# for move in move_list:
#     if move == 'L':
#         start[1] -= 1
#     elif move == 'R':
#         start[1] += 1
#     elif move == 'U':
#         start[0] -= 1
#     else:
#         start[0] += 1

#     for i in range(2):
#         start[i] = start[i] + 1 if start[i] < 1 else start[i]
#         start[i] = start[i] - 1 if start[i] > n else start[i]
    
# print(*start)

n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        x, y = nx, ny

print(x, y)