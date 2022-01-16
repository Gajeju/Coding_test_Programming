n = 1000 - int(input())

yen = [500,100,50,10,5,1]
count = 0

for coin in yen:
    count += n // coin
    n %= coin
        
print(count)


# 1000엔 지폐를 냈을때 거스름 동전 최소화
# 500엔 / 100엔 / 50엔 / 10엔 / 5엔 / 1엔
# 물건 가격은 1엔 이상 1000엔 미만