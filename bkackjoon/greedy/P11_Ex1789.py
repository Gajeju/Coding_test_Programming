s = int(input())
answer = 0

for i in range(s):
    answer += i
    if answer > s:
        break

print(i - 1)

# 서로다른 자연수 N의 합은 S
# N의 최댓값을 구하라
# 1부터 더하다가 s보다 커지면 하나를 빼고 하나를 고치면 완성할 수 있다.
# https://www.acmicpc.net/problem/1789