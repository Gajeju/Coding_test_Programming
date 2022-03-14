# 3인 체조 경기는 이번에 올림픽에 등록된 종목입니다.
# 경기를 하려면 3명의 선수가 필요합니다. 
# 3명의 선수가 한 칸씩 일렬로 서 있을 때 가운데에 서있는 선수를 제외한 나머지 두 선수 중 한 명이 나머지 두 사람 사이의 아무 칸으로 점프합니다.
#  이후 계속해서 기존의 두 선수 사이의 공간을 한 칸씩 점프하여 이동할 수 있습니다.
#  한 칸에 두 명 이상이 있을 수 없다고 할 때, 최대 몇 번의 점프를 할 수 있는지 알아내는 프로그램을 만드세요.

import sys
input = lambda : sys.stdin.readline().strip()

gymnasts = list(map(int, input().split()))
cnt = 0

while True:
    if gymnasts[0] + 2 == gymnasts[1] + 1 == gymnasts[2]:
        break
    
    if gymnasts[1] - gymnasts[0] > gymnasts[2] - gymnasts[1]:
        gymnasts[2] = gymnasts[0] + 1
        cnt += 1
    else:
        gymnasts[0] = gymnasts[2] - 1
        cnt += 1
    gymnasts.sort()
    
print(cnt)