prime_list = [False, False] + [True]*10002

for i in range(2, 10002):
    if prime_list[i]:
        for j in range(2*i, 10002, i):
            prime_list[j] = False

T = int(input())

for i in range(T):
    n = int(input())
    a = n//2
    b = a
    while a>0:
        if prime_list[a] and prime_list[b]:
            print(a, b)
            break
        else:
            a-=1
            b+=1


# 고드바흐
# 2보다 큰 짝수는 두 소수의 합으로 나탸낼 수 있다.
# 만약 골드바흐 파티션이 여러 가지인 경우 두 소수의 차이가 가장 자은 것을 출력
# 4 <= n <= 10000
# 작은것부터 출력
# # 테스트 케이스

# https://www.acmicpc.net/problem/9020