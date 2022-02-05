n = int(input())
meetings = [list(map(int, input().split())) for _ in range(n)]
meetings.sort(key=lambda x: (x[1], x[0]))

count = 0
before = -1

for time in meetings:
    if time[0] >= before:
        count += 1
        before = time[1]

print(count)

# N 회의 개수
# 회의 시간이 겹치지 않으면서 회의개수 최대
# 일찍 끝나는 회의를 겹치지 않게 선택