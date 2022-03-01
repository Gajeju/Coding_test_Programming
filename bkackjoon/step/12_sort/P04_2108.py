from collections import Counter
import sys

n = int(sys.stdin.readline())
n_list = [int(sys.stdin.readline()) for _ in range(n)]

# 산술평균
print(round(sum(n_list) / len(n_list)))

# 중앙값
n_list.sort()
print(n_list[len(n_list) // 2])

# 최빈값
cnt = Counter(n_list).most_common(2)
if len(n_list) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])


# 범위
print(max(n_list) - min(n_list))

# n은 홀수
# 산술평균 : sum(n) / n
# 중앙값 정렬 후 가운데
# 최빈값 : 가장 많은 값
# 범위 : 최댓값과 최솟값의 차이

# https://www.acmicpc.net/problem/2108