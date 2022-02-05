N = int(input())
Pi = list(map(int,  input().split(' ')))

Pi.sort()
answer = 0

for i in range(N):
    for j in range(i+1):
        answer += Pi[j]

print(answer)

# 줄서는 시간의 합 최소화