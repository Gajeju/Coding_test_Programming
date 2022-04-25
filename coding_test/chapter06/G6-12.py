# 두 개의 배열 A B
# N개의 원소로 구성
# 원소 모두 자연수
# K번의 바꿔치기 연산 진행
# A배열에 있는 원소의 합이 최대

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i] = b[i]
    else:
        break

print(sum(a))