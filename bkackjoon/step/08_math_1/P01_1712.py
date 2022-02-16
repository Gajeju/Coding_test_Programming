a,b,c = map(int, input().split())

if b >= c:
    print(-1)
    exit()

n = (a // (c -b)) + 1
print(n) 


# 손익분기점
# 고정비용 A만원
# 노트북 1대 생산 가변비용 B만원
# 노트북 가격 C만원

# 총 비용 = A + (B * n)
# 이익 = C * n

# https://www.acmicpc.net/problem/1712