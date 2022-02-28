n = int(input())
peo = [list(map(int, input().split())) for _ in range(n)]


for per1 in peo:
    cnt = 1
    for per2 in peo:
        if per1[0] < per2[0] and per1[1] < per2[1]:
            cnt += 1
    print(cnt)




# 덩치 =  (몸무게, 키)
# 키 몸무게 둘 다 크면 덩치가 더 크다
# 덩치 등수 계산해서 출력

# https://www.acmicpc.net/problem/7568