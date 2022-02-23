def fibonacci(n):
    if n == 0: return 0
    if n == 1: return 1
    return fibonacci(n-2) + fibonacci(n-1)

n = int(input())
print(fibonacci(n))

# 피보나치
# 0 1로 시작
# https://www.acmicpc.net/problem/10870