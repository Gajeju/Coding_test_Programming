N = input()
n = int(N)
sug5 = 0
sug3 = 0

if n % 5 == 0:
    print(n // 5)
    exit()
     
while n > 2:
    if n % 3 == 0:
        sug3 = n // 3
    n -= 5
sug5 = (int(N) - (sug3 * 3)) / 5

if sug5 % 1 != 0:
    print(-1)
else:
    print(int(sug5) + sug3)

# 설탕 배달
# 설탕 5키로 3키로를 가지고 최소개수 정확히 나누어 떨어져야 함