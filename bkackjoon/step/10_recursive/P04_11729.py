def hanoi(n, x, y):
    if n > 1:
        hanoi(n-1, x, 6-x-y)

    print(x, y)
    
    if n > 1:
        hanoi(n- 1, 6 - x - y, y)

    
n = int(input())
print(2**n-1)
hanoi(n, 1, 3)


# n 원판의 개수 (1 <= n <= 20)
# 첫째줄 옮긴 횟수 k 출력
# 둘재줄부터 과정 출력 1 3 : 1번 기둥의 원판을 3번에 옮긴다.

# 맨 마지막을 제외하고 목표 기둥 외의 다른 기둥에 옮긴다 -> 맨 마지막 원반을 옮긴다  -> 나머지 원반을 목표 기등에 옮긴다

# https://www.acmicpc.net/problem/11729