n = int(input())
road = list(map(int, input().split()))
oil_price = list(map(int, input().split()))

min_oil = oil_price[0]
total = 0

for i in range(n-1):
    if oil_price[i] < min_oil:
        min_oil = oil_price[i]
    total += road[i] * min_oil

print(total)



# 주유소 도시개수 N개 도로 개수 N-1개
# 1km 당 1리터의 기름을 사용하며 처음에는 기름이 없는 상태에서 시작
# 기름 가격은 도시마다 다르며 최소가격으로 마지막 도시 도달

# 이미 지나온 도시 중 앞 도시보다 기름이 싼 곳이 있으면 거기서 주유한 것으로 계산한다

# https://www.acmicpc.net/problem/13305