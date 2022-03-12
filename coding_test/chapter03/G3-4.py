# n == 1 이 될 때까지 연산 반복
# 1. N에서 1을 뺀다
# 2. N을 K로 나눈다 단, 나누어 떨어질때만 가능
# 최소 횟수 구하기

# 2 <= n M- 100,000 2 <= k <= 100,000

import time

start_time = time.time()

n, k = map(int, input().split())
cnt = 0
while n > 1:
    if n % k == 0:
        n //= k
        cnt += 1
    else:
        n -= 1
        cnt += 1
print(cnt)


end_time = time.time()
print(f'time: {end_time - start_time}')