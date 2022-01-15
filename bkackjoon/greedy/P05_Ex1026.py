n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

sum = 0

for i in range(n):
    sum += min(a) * max(b)
    a.remove(min(a))
    b.remove(max(b))

print(sum)




 # 배열길이 N
 # A 를 정렬해서 A, B의 원소간 곱의 합을 최소로 만들기
 # B원소의 최댓값에 A원소의 최솟값이 배치되게 한다
