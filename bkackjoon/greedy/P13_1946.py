t = int(input())

for _ in range(t):
    n = int(input())
    applicants = [tuple(map(int, input().split())) for _ in range(n)]
    applicants.sort()

    interview = applicants[0][1]
    cnt = 1

    for a in applicants:
        if interview > a[1]:
            cnt += 1
            interview = a[1]

    print(cnt)



# 면접
# 다른 지원자와 비교하여 두 성적 모두 뒤처지면 떨어진다
# 첫줄 테스트 갯수 T
# 둘째줄 지원자 수
# 셋째줄부터 순위, 동순위 없음

# 서류 순으로 정렬하고 대상보다 서류 순위가 높은 사람이랑 대상의 면접을 비교

#  sys.stdin.readline() 사용시 시간초과 막을 수 있다

# https://www.acmicpc.net/problem/1946