# 시각
# 정수 N이 입력되면 N시 59분 59초까지 몯느 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하시오
import sys

n = int(sys.stdin.readline())
cnt = 0

for hour in range(n+1):
    for time in range(60):
        for sec in range(60):
            if '3' in str(hour) + str(time) + str(sec):
                cnt += 1

print(cnt)



