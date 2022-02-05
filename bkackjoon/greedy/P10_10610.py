n = list(map(int, input()))

if sum(n) % 3 == 0 and 0 in n:
    n.sort(reverse=True)
    print(*n, sep='')
else:
    print(-1)


# 양수 n으로 가장 큰 30의 배수 만들기
# n은 최대 10^5자리수이며, 0으로 시작하지 않은다.
# 30의 배수에 필요한 요소가 있는지 확인하고 점점 큰 수를 확인, count를 써서 했으나 탈출조건을 만들 수 없음
# 30의 배수는 각 자리의 합이 3의 배수이고 끝자리가 0이어야 한다
# https://www.acmicpc.net/problem/10610