n, m = map(int, input().split())
cards = list(map(int, input().split()))
tot = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            tmp = cards[i] + cards[j] + cards[k]
            if tmp > m:
                continue
            else: tot = tot if tot > tmp else tmp

print(tot)


# 블랙잭 카드합이 m을 넘지 않으면서 카드 합을 최대로 만든다
# n 카드 장 수  m 최대합
# 3장을 뽑아 m을 넘지 않으면서 최대 만들기

# https://www.acmicpc.net/problem/2798