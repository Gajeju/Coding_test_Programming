n = int(input())
rope = [int(input()) for _ in range(n)]

rope.sort(reverse=True)
weight = rope[0]

for i in range(1, n):
    if weight < rope[i] * (i+1):
        weight = rope[i] * (i+1)

print(weight)


# n은 로프의 개수
# 로프는 중량을 나눠들 수 있으며 중량은 로프의 종류와 관계없이 똑같이 나뉜다
# 개수를 늘리는 것이 의미가 없어질 때까지 무거운거부터 하나식 추가
# https://www.acmicpc.net/problem/2217