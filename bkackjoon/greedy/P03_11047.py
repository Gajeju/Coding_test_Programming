n, k = map(int, input().split())

coins = []
coin = 0

for i in range(n):
    coins.append(int(input()))


coins.reverse()

for i in coins:
    if k // i != 0:
        coin += k // i
        k %= i

print(coin)

# 가지고 있는 동전 N종류
# K 동전 가치의 합, 최소 동전
