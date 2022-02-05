t = int(input())
time_table = [300, 60, 10]
counts = []

for i in time_table:
    counts.append(t // i)
    t %= i

if t != 0:
    print(-1)
else:
    print(*counts)

# A B C 5분 1분 10초
# 최소 버튼 입력, 맞출 수 없으면 -1 
# 입력 T는 초 단위로 주어진다
# https://www.acmicpc.net/problem/10162