n = int(input())

cnt = 1
bee = 1

while n > bee:
    bee += 6 * cnt
    cnt += 1

print(cnt)
    


# 6각형 벌집에서 N번 방까지 최소 개수의 방을 지나서 갈 때 최소개수

# 1 6 12 18 24
# 6 * 2^(n-1)

# https://www.acmicpc.net/problem/2292