# 왕실의 나이트
# 채스판 위의 나이트의 위치가 주어졌을 때 움직일 수 있는 경우의 수 출력
import sys

n = sys.stdin.readline().strip()
cood = [ord(n[0])-97, int(n[1:])-1]

move_list = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]
cnt = 0

for move in move_list:
    tmp = [cood[0]+move[0], cood[1]+move[1]]
    if (-1<tmp[0]<8) and (-1<tmp[1]<8):
        cnt += 1


print(cnt)